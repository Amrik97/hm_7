class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            "wage": wage,
            "bonus": bonus
        }


class Position(Worker):

    def get_full_name(self):
        self.full_name = self.name + " " + self.surname
        return self.full_name

    def get_total_income(self):
        self.total_income = self._income["wage"] + self._income["bonus"]
        return self.total_income

    def __str__(self):
        return "Full name: {} \nPosition: {} \nIncome: {}".format(self.get_full_name(), self.position,
                                                                  self.get_total_income())


if __name__ == '__main__':
    a = Position("John", "Stacy", "Loyer", 120000, 100000)
    print(a)
