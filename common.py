from datetime import datetime
from math import floor
class Timer():
    def __init__(self):
        self.startTime = datetime.now()
        self.endTime = None
    def stop(self, out=True):
        self.endTime = datetime.now() - self.startTime
        if out:
            if self.endTime.total_seconds() < 1:
                if self.endTime.total_seconds() < 0.001:
                    print(round(self.endTime.total_seconds()*1000000), 'μs')
                elif self.endTime.total_seconds() < 0.01:
                    print(round(self.endTime.total_seconds()*1000, 2), 'ms')
                else:
                    print(round(self.endTime.total_seconds()*1000), 'ms')
            elif self.endTime.total_seconds() < 60:
                print(str(round(self.endTime.total_seconds()) % 60), 's')
            else:
                print(str(floor(self.endTime.total_seconds()/60)) + ':' + str(round(self.endTime.total_seconds()) % 60))
    def restart(self):
        self.__init__()

def load_day(num, example=None, lines=True, map=False):
    if example == None:
        example = input("Enter for example, anything else for non-example >") == ""
    with open(f'inputs/day{num}{"example" if example else ""}.txt', 'r') as f:
        if map:
            return [list(line) for line in f.read().splitlines()]
        elif lines:
            return f.read().splitlines()
        else:
            return f.read()

def print_list(input):
    for line in input:
        print(''.join(line))

def print_result(result):
    if result == list:
        print_list(result)
    else:
        print(result, end=" -- ", flush=False)