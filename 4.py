class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} начало движения')

    def stop(self):
        print(f'{self.name} остановка')

    def turn(self, direction):
        print(f'{self.name} поворот на  {self.name ,direction}!')

    def show_speed(self):
        print('Скорость равна: ',self.speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Предупреждение ! Сбавьте скорость')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print('Current speed:', self.speed)
        if self.speed > 40:
            print('Предупреждение ! Сбавьте скорость')


class PoliceCar(Car):
    pass


sport_car = SportCar(180, "чёрная", 'Спортивная машина', False)
town_car = TownCar(140, 'белая', 'машина для города', False)
work_car = WorkCar(90, 'Желтая', 'спец средство', False)
police_car = PoliceCar(120, 'Синяя', 'Полиция', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
town_car.turn('Право')