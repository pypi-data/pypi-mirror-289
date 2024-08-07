import pandas as pd
# from config import CONSOLE_MODE

# region Monitor
class Monitor(object):
    def __init__(self, filepath):
        """
        Monitor 클래스 초기화 메서드
        :: 주어진 파일 경로를 사용하여 이벤트 트레이서를 초기화 함

        ### Args:
            - `filepath (str)`: 이벤트 트레이서를 저장할 파일 경로
        """
        
        self.filepath = filepath  ## Event tracer 저장 경로
        # 이벤트 데이터 저장할 리스트 초기화(시간, 사건, 부품, 공정이름, 기계 이름)
        self.time = list()
        self.event = list()
        self.part = list()
        self.process_name = list()
        self.machine_name = list()

    def record(self, time, process, machine, part_name=None, event=None):
        """
        기록 메서드
        :: 주어진 시간, 공정, 기계, 부품 이름 및 이벤트를 기록함

        ### Args:
            - `time (str)`: 기록할 시간 정보
            - `process (str)`: 기록할 공정의 이름
            - `machine (str)`: 기록할 기계의 이름
            - `part_name (str, optional)`: 기록할 부품의 이름, 기본값은 None
            - `event (str, optional)`: 기록할 이벤트의 이름, 기본값은 None
        """
        self.time.append(time)
        self.event.append(event)
        self.part.append(part_name)  # string
        self.process_name.append(process)
        self.machine_name.append(machine)

    def save_event(self):
        """
        기록된 이벤트를 저장하는 메서드
        :: 모든 기록된 이벤트를 CSV 파일로 저장하고 데이터프레임을 반환함

        ### Returns:
            - `pd.DataFrame`: 기록된 이벤트를 포함하는 데이터프레임
        """
        event = pd.DataFrame(columns=['Time', 'Event', 'Part', 'Process', 'Machine'])
        event['Time'] = self.time
        event['Event'] = self.event
        event['Part'] = self.part
        event['Process'] = self.process_name
        event['Machine'] = self.machine_name

        event.to_csv(self.filepath) # dataframe 데이터를 CSV 파일 형식으로 저장

        return event


# endregion

def monitor_console(time, part, object='Entire Process', command=''):
    """
    제조 공정 이벤트를 콘솔에 출력하는 함수
    :: 특정 시간에 어떤 부품이 어떤 공정을 거치고 있는지, 그 공정이 어느 기계에서 실행되고 있는지에 대한 정보를 출력함

    ### Args:
        - `time (str)`: 이벤트 발생 시간
        - `part (object)`: 현재 작업 중인 부품에 대한 정보
        - `object (str, optional)`: 출력할 정보의 범위. 'Single Part', 'Single Job', 'Entire Process', 'Machine' 중 하나를 지정. 기본값은 'Entire Process'
        - `command (str, optional)`: 추가로 출력할 명령이나 메시지. 기본값은 ''
    """
    # 제조 공정에서 발생하는 이벤트를 콘솔에 출력하는 역할을 함. / 진행상황을 쉽게 파악하기 위함
    # 특정 시간에 어떤 부품이 어떤 공정을 거치고 있는지, 그 공정이 어느 기계에서 실행되고 있는지에 대한 정보 출력.
    # time: 이벤트 발생시간, part: 현재 작업중인 부품에 대한 정보, object: 출력할 정보의 범위를 지정(ex) '단일부품', '전체공정')
    # command: 추가적으로 출력할 특별한 명령이나 메시지 지정 문자열.
    
    # console_mode : boolean
    # object : 'single part' for default
    
    operation = part.op[part.step]
    command = " "+command+" "
    if object == 'Single Part':
        # 단일 부품에 대한 정보만 출력. 특정 부품의 현재 공정과 그 공정이 실행되는 기계이름 출력
        print(str(time), '\t', operation.name, command,end='')
        print(operation.machine)
    elif object == 'Single Job':
        # 작업의 시작 부분만을 특별히 강조하여 출력. 주로 특정 작업의 첫번째 부품만을 출력하는데 사용.
        if operation.part_name == 'Part0_0':
            print(str(time), '\t', operation.name, command,end='')
        print(operation.machine)
    elif object == 'Entire Process':
        # 전체 공정에 대한 정보 출력. 모든 부품과 관련된 모든 공정을 시간 순으로 출력하여 전체제조과정 흐름 파악
        print(str(time), '\t', operation.name, command, operation.machine_determined.name)
    elif object == 'Machine':
        # 기계 별로 이벤트 정보를 출력. 각 기계에서 실행되고 있는 공정의 이름을 각기 다른 포맷으로 출력, 어떤 기계가 어떤 작업하는지 쉽게 구분.
        print_by_machine(time, part)


def print_by_machine(env, part):
    """
    기계 별로 이벤트 정보를 출력하는 함수
    :: 각 기계에서 실행되고 있는 공정의 이름을 포맷에 맞게 출력함

    ### Args:
        - `env (object)`: 현재 환경 또는 시뮬레이션 객체, 현재 시간 제공
        - `part (object)`: 현재 작업 중인 부품에 대한 정보
    """
    if part.op[part.step].machine_list == 0:
        print(str(env.now), '\t\t\t\t', str(part.op[part.step].name))
        # \t는 tap 의미.
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
