"""
Test Case에 대해 monitor class log, Gantt Chart, GUI 창을 띄우는 코드
"""
from environment.source import Source
from environment.sink import Sink
from environment.process import Process
from environment.resource import Machine
from environment.monitor import Monitor
from postprocessing.postprocessing import *
from Data.Adams.abz6.abz6 import Dataset
from visualization.Gantt import *
from visualization.GUI import GUI
import simpy, os
import datetime
from utils import *
from Config.Run_Config import Run_Config
SIMUL_TIME = 10000

if __name__ == "__main__":
    
    
    # Directory Configuration
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define the folder name
    folder_name = 'result'

    # Construct the full path to the folder
    save_path = os.path.join(script_dir, folder_name)

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    now = datetime.datetime.now()
    filename = now.strftime('%Y-%m-%d-%H-%M-%S')
    filepath = os.path.join(save_path, filename + '.csv')

    data = Dataset()
    config = Run_Config(data.n_job, data.n_machine, data.n_op, False, True,
                        True, True, True, True)

    seq = [i for i in range(data.n_op)]
    job_seq = get_repeatable(seq, config)
    feasible_seq = get_feasible(seq, config)
    machine_seq = get_machine_order(feasible_seq, config, data.op_data, job_seq)

    env = simpy.Environment()
    monitor = Monitor(config)
    model = dict()
    for i in range(config.n_job):
        model['Source' + str(i)] = Source(env, 'Source' + str(i), model, monitor,
                                          part_type=i, op_data=data.op_data, config=config)

    for j in range(config.n_machine):
        model['Process' + str(j)] = Process(env, 'Process' + str(j), model, monitor, machine_seq[j],
                                            config)
        model['M' + str(j)] = Machine(env, j)

    model['Sink'] = Sink(env, monitor, config)

    # In case of the situation where termination of the simulation greatly affects the machine utilization time,
    # it is necessary to terminate all the process at (SIMUL_TIME -1) and add up the process time to all machines
    env.run(config.simul_time)

    if config.save_log:
        monitor.save_event_tracer()
        if config.save_machinelog:
            machine_log_ = machine_log(config)
            if config.save_machinelog & config.show_gantt:
                gantt = Gantt(machine_log_, len(machine_log_), config)
                if config.show_gui:
                    gui = GUI(gantt)

    # In case of the situation where termination of the simulation greatly affects the machine utilization time,
    # it is necessary to terminate all the process at (SIMUL_TIME -1) and add up the process time to all machines

    # 어떤 machine M1이 t=1000부터 t=2500까지 작업 중이라면 임의로 simul_time = 2000까지 지정해서 실행할 경우,
    # 이 machine의 작업 log는 t=1000에 시작한 작업이 반영되지 않아서 utilization이 50% 미만으로 계산될 수 있음.
    # 따라서 작업이 완료되지 않았더라도 t=1000~1999까지는 작업중이었다는 것을 명시하는 코드가 추가로 필요함. (아직 반영 전)

    print()
