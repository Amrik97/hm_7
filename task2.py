class Road:
    _length = 20
    _width = 5000
    weigh = 25
    num_m = 0.05

    def __init__(self, length, width, weigh, num_m):
        self._length = length
        self._width = width
        self.weigh = weigh
        self.num_m = num_m

    def weight_culculator(self):
        res = self._length * self._width * self.weigh * self.num_m
        if res >= 100 and res < 1000:
            print(str(self._length) + "м * " + str(self._width) + "м * " + str(self.weigh) + "кг * " + str(self.num_m) + "м = " + str(res / 100) + "ц")
        elif res >= 1000:
            print(str(self._length) + "м * " + str(self._width) + "м * " + str(self.weigh) + "кг * " + str(self.num_m) + "м = " + str(res / 1000) + "т")
        else:
            print(str(self._length) + "м * " + str(self._width) + "м * " + str(self.weigh) + "кг * " + str(self.num_m) + "м = " + str(res) + "кг")


if __name__ == '__main__':
    a = Road(20, 5000, 25, 0.05)
    a.weight_culculator()