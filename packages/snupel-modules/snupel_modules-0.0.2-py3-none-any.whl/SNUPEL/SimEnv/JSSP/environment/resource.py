"""
This script is declaration of Resource object in the environment of JSSP.
Last revised by Jiwon Baek (baekjiwon@snu.ac.kr)
August 2nd. 2024.
"""

import simpy
class Machine(object):
    def __init__(self, env, id):
        """An example of a resource-type Class object"""
        self.env = env
        self.id = id
        self.capacity = 1
        self.availability = simpy.Store(env, capacity=self.capacity)
        self.workingtime_log = []
        self.util_time = 0.0
        self.op_where = []

    def add_reference(self, op):
        self.op_where.append(op.id) # 처리한 op가 몇 번째였는지를 기록


class Worker(object):
    def __init__(self, env, id):
        self.env = env
        self.id = id
        self.capacity = 1
        self.availability = simpy.Store(env, capacity=self.capacity)
        self.workingtime_log = []
        self.util_time = 0.0


class Jig(object):
    def __init__(self, env, id):
        self.env = env
        self.id = id
        self.capacity = 1
        self.availability = simpy.Store(env, capacity=self.capacity)
        self.workingtime_log = []
        self.util_time = 0.0
