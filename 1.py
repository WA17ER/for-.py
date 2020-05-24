import time
import itertools

my_trafick_data = [("red", 7), ("yelow",2),("green",9)]

class TrafficLight :
    def __init__(self):
        global my_trafick_data
        self.__color = my_trafick_data

    def running(self):
        for color, sec in itertools.cycle(self.__color):
            print(f'{color}')
            time.sleep(sec)


launch = TrafficLight()
launch.running()

