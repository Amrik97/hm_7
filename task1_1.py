import time


class TrafficLight:
    __color = "red"

    def __init__(self, color):
        self.__color = color

    def running(self):
        self.__color = "red"
        print(self.__color)
        time.sleep(7)
        self.__color = "yellow"
        print(self.__color)
        time.sleep(2)
        self.__color = "green"
        print(self.__color)
        time.sleep(10)


if __name__ == '__main__':
    a = TrafficLight
    a.running(a)
    exit(0)