from car import Car


class ElectricCar(Car):
    """ представляет аспекты машины, специфияеские для электромобилей"""

    def __init__(self, make, model, year):
        """инициализирует атрибуты класса-родителя
        Затем иниц. атрибуты, специфические для электромобилей"""
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """Выводит информацию о батарее"""
        print('Этот автомобиль имеет мощность батареи ' +
              str(self.battery_size) + ' кВт')
