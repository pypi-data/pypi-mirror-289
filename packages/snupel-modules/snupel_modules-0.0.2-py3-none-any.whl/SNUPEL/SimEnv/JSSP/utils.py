"""
JSSP 환경을 구동하기 위해 필요한 sequence 관련 operation 함수들을 모아 놓은 스크립트.
근데 n_machine = 10 일 떄만 동작하는 것 같음. 
다른 n_machine을 했을 때 돌아가는지는 장담 못함.
Last revised by Jiwon Baek (baekjiwon@snu.ac.kr)
August 2nd. 2024.
"""

import numpy as np


def swap_digits(num, n_machine=10):
    if num < n_machine:
        return num * n_machine
    else:
        units = num % n_machine
        tens = num // n_machine
        return units * n_machine + tens


def interpret_solution(s, n_machine=10):
    # 리스트의 각 원소에 대해 숫자 바꾸기
    modified_list = [swap_digits(num, n_machine) for num in s]
    return modified_list


def get_repeatable(seq, config):
    cumul = 0
    sequence_ = np.array(seq)
    for i in range(config.n_job):
        for j in range(config.n_machine):
            sequence_ = np.where((sequence_ >= cumul) &
                                 (sequence_ < cumul + config.n_machine), i, sequence_)
        cumul += config.n_machine
    sequence_ = sequence_.tolist()
    return sequence_


def get_feasible(seq, config):
    temp = 0
    cumul = 0
    sequence_ = np.array(seq)
    for i in range(config.n_job):
        idx = np.where((sequence_ >= cumul) & (sequence_ < cumul + config.n_machine))[0]
        for j in range(config.n_machine):
            sequence_[idx[j]] = temp
            temp += 1
        cumul += config.n_machine
    return sequence_


def get_machine_order(feasible_seq, config, op_data, job_seq):
    m_list = []
    for num in feasible_seq:
        idx_j = num % config.n_machine  # job의 번호
        idx_i = num // config.n_machine
        m_list.append(op_data[idx_i][idx_j][0])
    m_list = np.array(m_list)

    m_order = []
    for num in range(config.n_machine):
        idx = np.where((m_list == num))[0]
        job_order = [job_seq[o] for o in idx]
        m_order.append(job_order)
    return m_order
