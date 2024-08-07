import pandas as pd

# from config import CONSOLE_MODE

# region Monitor
class Monitor(object):
    """
    시뮬레이션의 이벤트를 기록하고 CSV 파일로 저장하는 클래스.

    ### Args:
        - `filepath (str)`: 이벤트 로그를 저장할 CSV 파일의 경로.
    """
    def __init__(self, filepath):
        self.filepath = filepath
        self.time = list()
        self.event = list()
        self.part = list()
        self.process_name = list()
        self.machine_name = list()

    def record(self, time, process, machine, part_name=None, event=None):
        """
        시뮬레이션 이벤트를 기록.

        ### Args:
            - `time (float)`: 이벤트 발생 시각.
            - `process (str)`: 이벤트가 발생한 공정의 이름.
            - `machine (str)`: 이벤트와 관련된 기계의 이름.
            - `part_name (str, optional)`: 이벤트와 관련된 부품의 이름. 기본값은 `None`.
            - `event (str, optional)`: 이벤트의 설명. 기본값은 `None`.
        """
        self.time.append(time)
        self.event.append(event)
        self.part.append(part_name)
        self.process_name.append(process)
        self.machine_name.append(machine)

    def save_event(self):
        """
        기록된 이벤트를 CSV 파일로 저장하고, 데이터프레임 형태로 반환.

        ### Returns:
            - `pd.DataFrame`: 기록된 이벤트의 데이터를 포함하는 Pandas 데이터프레임.
        """
        event = pd.DataFrame(columns=['Time', 'Event', 'Part', 'Process', 'Machine'])
        event['Time'] = self.time
        event['Event'] = self.event
        event['Part'] = self.part
        event['Process'] = self.process_name
        event['Machine'] = self.machine_name
        event.to_csv(self.filepath)
        return event

# endregion

# 간단한 부품과 공정 예시
class Part:
    def __init__(self):
        self.step = 0
        self.op = [{
            'name': 'Drilling',
            'machine': 'Drill Press',
            'machine_determined': {'name': 'Drill Press 1'},
            'machine_list': 1,
            'part_name': 'Part0_0'
        }]

# Monitor 인스턴스 생성 및 이벤트 기록
monitor = Monitor('events.csv')
monitor.record(time="10:00", process="Start", machine="Drill Press", part_name="Part0_0", event="Begin Operation")
monitor.record(time="10:30", process="Check", machine="Drill Press", part_name="Part0_0", event="Mid Operation")
monitor.record(time="11:00", process="End", machine="Drill Press", part_name="Part0_0", event="End Operation")
monitor.save_event()

# 이벤트를 콘솔에 출력
def monitor_console(time, part, object='Entire Process', command=''):
    """
    시뮬레이션 이벤트를 콘솔에 출력.

    ### Args:
        - `time (str)`: 이벤트 발생 시각.
        - `part (Part)`: 이벤트와 관련된 부품 객체.
        - `object (str, optional)`: 출력할 정보의 종류를 지정. 기본값은 'Entire Process'.
        - `command (str, optional)`: 이벤트에 대한 추가 설명. 기본값은 ''.
    """
    operation = part.op[part.step]
    command = " "+command+" "
    if object == 'Single Part':
        print(str(time), '\t', operation.name, command, operation.machine)
    elif object == 'Single Job':
        if operation.part_name == 'Part0_0':
            print(str(time), '\t', operation.name, command, operation.machine)
    elif object == 'Entire Process':
        print(str(time), '\t', operation.name, command, operation.machine_determined['name'])
    elif object == 'Machine':
        print_by_machine(time, part)

def print_by_machine(env, part):
    """
    기계별로 부품의 처리 상태를 콘솔에 출력.

    ### Args:
        - `env (simpy.Environment)`: SimPy 환경 객체.
        - `part (Part)`: 이벤트와 관련된 부품 객체.
    """
    if part.op[part.step].machine_list == 0:
        print(str(env.now), '\t\t\t\t', str(part.op[part.step].name))
    elif part.op[part.step].machine_list == 1:
        print(str(env.now), '\t\t\t\t\t\t\t', str(part.op[part.step].name))
    elif part.op[part.step].machine_list == 2:
        print(str(env.now), '\t\t\t\t\t\t\t\t\t\t', str(part.op[part.step].name))
    elif part.op[part.step].machine_list == 3:
        print(str(env.now), '\t\t\t\t\t\t\t\t\t\t\t\t\t', str(part.op[part.step].name))
    elif part.op[part.step].machine_list == 4:
        print(str(env.now), '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t', str(part.op[part.step].name))
    else:
        print()

# 가상의 시간과 부품 객체를 사용하여 함수를 시험
part_example = Part()
monitor_console("10:00", part_example, "Entire Process", "Operation Started")