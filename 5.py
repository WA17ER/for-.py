class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Выбор инструмента')


class Pen(Stationery):
    def draw(self):
        print('Используется ручка')


class Pencil(Stationery):
    def draw(self):
        print('используется карандаш')


class Handle(Stationery):
    def draw(self):
        print('используется маркер')