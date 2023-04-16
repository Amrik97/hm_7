import time


class TrafficLight:
    __color = "red"

    def __init__(self, color):
        self.__color = color

    def running(self):
        if self.__color == "red":
            print(self.__color)
            time.sleep(7)
            self.__color = "yellow"
            print(self.__color)
            time.sleep(2)
            self.__color = "green"
            print(self.__color)
            time.sleep(10)
        elif self.__color == "yellow":
            print(self.__color)
            time.sleep(2)
            self.__color = "green"
            print(self.__color)
            time.sleep(10)
            self.__color = "red"
            print(self.__color)
            time.sleep(7)
        elif self.__color == "green":
            print(self.__color)
            time.sleep(10)
            self.__color = "red"
            print(self.__color)
            time.sleep(7)
            self.__color = "yellow"
            print(self.__color)
            time.sleep(2)


if __name__ == '__main__':
    a = TrafficLight("green")  # В качестве параметра color для класса TrafficLight можно указать green, red или yellow
    a.running()
    exit(0)