import os
import numpy as np
import simpy
# from environment.simulation import *
from simulation import *


class PMSP:
    def __init__(self, num_job=200, num_m=5, episode=1, test_sample=None, reward_weight=None, rule_weight=None,
                 ddt=None, pt_var=None, is_train=True):
        self.num_job = num_job  # scheduling 대상 job의 수
        self.num_m = num_m  # parallel machine 수
        self.episode = episode
        self.test_sample = test_sample
        self.reward_weight = reward_weight if reward_weight is not None else [0.5, 0.5]
        self.rule_weight = rule_weight

        # self.ddt = 2.0
        if is_train:
            self.ddt = np.random.uniform(low=0.8, high=1.2)
            self.pt_var = np.random.uniform(low=0.1, high=0.5)
        else:
            self.ddt = ddt
            self.pt_var = pt_var

        # self.pt_var = 0.25
        # self.ddt = 0.9
        self.is_train = is_train

        self.state_dim = 2 * num_m + 8
        self.action_dim = 4

        self.mapping = {0: "SSPT", 1: "ATCS", 2: "MDD", 3: "COVERT"}
        self.time = 0
        self.previous_time_step = 0

        self.time_list = list()
        self.tardiness_list = list()
        self.setup_list = list()

        self.done = False
        self.time = 0
        self.reward_setup = 0
        self.reward_tard = 0

        # Debugging variables
        self.calling_line = None
        self.calling_setting = None
        self.input_queue = None
        self.n_route = 0
        self.recent_tardy = []
        self.n_tardy_in_queue = 0

        self.sim_env, self.model, self.source, self.sink, self.routing, self.monitor = self._modeling()

    def step(self, action):
        done = False
        self.previous_time_step = self.sim_env.now
        routing_rule = self.mapping[action]

        self.routing.decision.succeed(routing_rule)
        self.routing.indicator = False
        if len(self.routing.is_tardy)>0:
            self.recent_tardy.append(self.routing.is_tardy[-1])
        else:
            self.recent_tardy.append(False)
        while True:
            if self.routing.indicator:
                if self.sim_env.now != self.time:
                    self.time = self.sim_env.now
                break

            if self.sink.completed == self.num_job:
                done = True
                self.sim_env.run()
                # if self.episode % 50 == 0:
                #     self.monitor.save_tracer()
                # # self.monitor.save_tracer()
                break

            if len(self.sim_env._queue) == 0:
                self.monitor.get_logs(file_path='log.csv')
            self.sim_env.step()

        reward = self._calculate_reward()
        next_state = self._get_state()
        self.n_route += 1

        return next_state, reward, done

    def _modeling(self):
        env = simpy.Environment()

        monitor = Monitor()
        monitor.reset()

        iat = 15 / self.num_m
        # iat = 20 / self.num_m

        model = dict()
        job_list = list()
        for j in range(self.num_job):
            job_name = "Job {0}".format(j)
            processing_time = np.random.uniform(10, 20) if self.test_sample is None else self.test_sample['processing_time'][j]
            feature = random.randint(0, 5) if self.test_sample is None else self.test_sample['feature'][j]
            job_list.append(Job(name=job_name, processing_time=processing_time, feature=feature))

        routing = Routing(env, model, monitor, end_num=self.num_job, weight=self.rule_weight)
        routing.reset()

        sink = Sink(env, monitor)
        sink.reset()

        source = Source(env, job_list, iat, self.ddt, routing, monitor)

        for m in range(self.num_m):
            machine_name = "Machine {0}".format(m)
            setup = random.randint(0, 5)  # initial setup
            model[machine_name] = Process(env, machine_name, routing, sink, monitor, pt_var=self.pt_var)
            model[machine_name].reset()

        return env, model, source, sink, routing, monitor

    def reset(self):
        self.episode = self.episode + 1 if self.episode > 1 else 1  # episode
        if self.is_train:
            """ DDT와 Processing time의 variance는 매 episode마다 reset됨"""

            self.pt_var = np.random.uniform(low=0.1, high=0.5)
            self.ddt = np.random.uniform(low=0.8, high=1.2)
            # self.pt_var = 0.25
            # self.ddt = 0.9

        self.sim_env, self.model, self.source, self.sink, self.routing, self.monitor = self._modeling()
        self.done = False
        self.reward_setup = 0
        self.reward_tard = 0
        self.monitor.reset()

        while True:
            # Check whether there is any decision time step
            if self.routing.indicator:
                break

            self.sim_env.step()

        return self._get_state()

    def count_tardy(self):
        self.n_tardy_in_queue = 0
        for job in self.input_queue:
            if job.due_date < self.sim_env.now:
                job.is_tardy = True
                self.n_tardy_in_queue += 1
        return self.n_tardy_in_queue
    def _get_state(self):
        self.n_tardy_in_queue = 0
        f_1 = np.zeros(self.num_m)  # Setup -> 현재 라인의 셋업 값과 같은 셋업인 job의 수
        f_2 = np.zeros(4)  # Due Date -> Tardiness level for non-setup
        f_3 = np.zeros(4)  # Due Date -> Tardiness level for setup
        f_4 = np.zeros(self.num_m)  # General Info -> 각 라인의 progress rate
        self.input_queue = copy.deepcopy(list(self.routing.queue.items))
        for line_num in range(self.num_m):
            line = self.model["Machine {0}".format(line_num)]
            same_setup_list = [1 for job in self.input_queue if job.feature == line.setup]
            f_1[line_num] = np.sum(same_setup_list) / len(self.input_queue) if len(self.input_queue) > 0 else 0.0

            if line.job is not None and not line.idle:  # 현재 작업 중인 job이 있을 때
                f_4[line_num] = (line.expected_finish_time - self.sim_env.now) / (
                            line.expected_finish_time - line.start_time)

        # feature 2, 3
        self.calling_line = self.model[self.routing.machine]
        self.calling_setting = self.calling_line.setup

        non_setup_list = list()
        setup_list = list()

        if len(self.input_queue)> 0:
            for job in self.input_queue:

                if job.feature == self.calling_setting:
                    non_setup_list.append(job)
                else:
                    setup_list.append(job)

        if len(non_setup_list) > 0:
            g_1 = 0
            g_2 = 0
            g_3 = 0
            g_4 = 0

            for non_setup_job in non_setup_list:
                job_dd = non_setup_job.due_date
                max_tightness = job_dd - (1 + self.pt_var) * non_setup_job.processing_time - self.sim_env.now
                min_tightness = job_dd - (1 - self.pt_var) * non_setup_job.processing_time - self.sim_env.now

                if max_tightness > 0:
                    g_1 += 1
                elif max_tightness <= 0 and min_tightness > 0:
                    g_2 += 1
                elif min_tightness <= 0 and self.sim_env.now > job_dd:
                    g_3 += 1
                elif self.sim_env.now < job_dd:
                    g_4 += 1
                else:
                    print(0)

            # f_2[0] = g_1 / len(non_setup_list)
            # f_2[1] = g_2 / len(non_setup_list)
            # f_2[2] = g_3 / len(non_setup_list)
            # f_2[3] = g_4 / len(non_setup_list)
            f_2[0] = g_1
            f_2[1] = g_2
            f_2[2] = g_3
            f_2[3] = g_4

        if len(setup_list) > 0:
            g_1 = 0
            g_2 = 0
            g_3 = 0
            g_4 = 0

            for setup_job in setup_list:
                job_dd = setup_job.due_date
                max_tightness = job_dd - (1 + self.pt_var) * setup_job.processing_time - self.sim_env.now
                min_tightness = job_dd - (1 - self.pt_var) * setup_job.processing_time - self.sim_env.now

                if max_tightness > 0:
                    g_1 += 1
                elif max_tightness <= 0 and min_tightness > 0:
                    g_2 += 1
                elif min_tightness < 0 and self.sim_env.now > job_dd:
                    g_3 += 1
                elif self.sim_env.now < job_dd:
                    g_4 += 1
                else:
                    print(0)

            # f_3[0] = g_1 / len(setup_list)
            # f_3[1] = g_2 / len(setup_list)
            # f_3[2] = g_3 / len(setup_list)
            # f_3[3] = g_4 / len(setup_list)
            f_3[0] = g_1
            f_3[1] = g_2
            f_3[2] = g_3
            f_3[3] = g_4
        state = np.concatenate((f_1, f_2, f_3, f_4), axis=None)
        return state

    def _calculate_reward(self):
        reward_1 = - self.routing.setup / 5
        self.reward_setup -= self.routing.setup / 5
        # reward_1 = 0.3 / self.routing.setup
        # self.reward_setup += 0.3 / self.routing.setup

        reward_2 = 0.0
        if len(self.sink.tardiness) > 0:
            for tardiness in self.sink.tardiness:
                # reward_2 += np.exp(-tardiness) - 1
                reward_2 += np.exp(-tardiness)

        # reward_2 = np.exp(-self.sink.tardiness) - 1
        self.reward_tard += reward_2

        reward = reward_1 * self.reward_weight[1] + reward_2 * self.reward_weight[0]
        self.routing.setup = 0
        self.sink.tardiness = list()
        return reward

    def get_logs(self, path=None):
        log = self.monitor.get_logs(path)
        return log

