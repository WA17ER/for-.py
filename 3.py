class Worker:
    def __init__(self, Name, Surname, position, income):
        self.name = Name
        self.surname = Surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name},{self.surname},{self.position},')

    def get_total_income(self):
        print(self._Worker__income['wage'] * self._Worker__income["bonus"])

zarplata = {'wage': 45000, 'bonus': 1.3}


test = Position('Ivanov','Sergey', 'jinior' , zarplata)
test.get_full_name()
test.get_total_income()
