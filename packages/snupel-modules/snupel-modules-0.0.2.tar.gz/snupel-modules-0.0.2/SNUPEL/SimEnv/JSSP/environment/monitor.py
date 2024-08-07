"""
This script is declaration of Monitor object in the environment of JSSP.
Last revised by Jiwon Baek (baekjiwon@snu.ac.kr)
August 2nd. 2024.
"""

import pandas as pd

# region Monitor
class Monitor(object):
    def __init__(self, config):
        """Initializes the Monitor object with the given configuration.

        Args:
            config (object): Configuration object containing settings for event tracer storage.
        """

        self.config = config  ## Event tracer 저장 경로
        self.time = list()
        self.event = list()
        self.part = list()
        self.process_name = list()
        self.machine_name = list()

    def record(self, time, process, machine, part_name=None, event=None):
        """Records an event with its associated details.

        Args:
            time (float): The time of the event.
            process (str): The name of the process.
            machine (str): The name of the machine.
            part_name (str, optional): The name of the part. Defaults to None.
            event (str, optional): The event description. Defaults to None.
        """
        self.time.append(time)
        self.event.append(event)
        self.part.append(part_name)  # string
        self.process_name.append(process)
        self.machine_name.append(machine)

    def save_event_tracer(self):
        """Saves the recorded events to a CSV file if logging is enabled in the configuration.

        Returns:
            pd.DataFrame: DataFrame containing all recorded events.
        """
        event_tracer = pd.DataFrame(columns=['Time', 'Event', 'Part', 'Process', 'Machine'])
        event_tracer['Time'] = self.time
        event_tracer['Event'] = self.event
        event_tracer['Part'] = self.part
        event_tracer['Process'] = self.process_name
        event_tracer['Machine'] = self.machine_name
        if self.config.save_log:
            event_tracer.to_csv(self.config.save_path + '\\' + self.config.filename['log'])

        return event_tracer


# endregion

def monitor_by_console(console_mode, env, part, object='Single Part', command=''):
    """Monitors and prints the event details to the console based on the specified mode and object.

    Args:
        console_mode (bool): Flag to enable or disable console output.
        env (object): The environment object containing the current simulation time.
        part (object): The part object containing the current operation details.
        object (str, optional): Specifies the object type for monitoring. Defaults to 'Single Part'.
        command (str, optional): Additional command to include in the console output. Defaults to ''.
    """
    if console_mode:
        operation = part.op[part.step]
        command = " " + command + " "
        if object == 'Single Part':
            if operation.process_type == 0:
                print(str(env.now) + '\t' + str(operation.name) + command + 'M' + str(operation.machine))
        elif object == 'Single Job':
            if operation.part_name == 'Part0_0':
                print(str(env.now) + '\t' + str(operation.name) + command + 'M' + str(operation.machine))
        elif object == 'Entire Process':
            print(str(env.now) + '\t' + str(operation.name) + command + 'M' + str(operation.machine))
        elif object == 'Machine':
            print_by_machine(env, part)


def print_by_machine(env, part):
    """Prints the event details by machine type to the console.

    Args:
        env (object): The environment object containing the current simulation time.
        part (object): The part object containing the current operation details.
    """
    if part.op[part.step].machine == 0:
        print(str(env.now) + '\t\t\t\t' + str(part.op[part.step].name))
    elif part.op[part.step].machine == 1:
        print(str(env.now) + '\t\t\t\t\t\t\t' + str(part.op[part.step].name))
    elif part.op[part.step].machine == 2:
        print(str(env.now) + '\t\t\t\t\t\t\t\t\t\t' + str(part.op[part.step].name))
    elif part.op[part.step].machine == 3:
        print(str(env.now) + '\t\t\t\t\t\t\t\t\t\t\t\t\t' + str(part.op[part.step].name))
    elif part.op[part.step].machine == 4:
        print(str(env.now) + '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t' + str(part.op[part.step].name))
    else:
        print()
