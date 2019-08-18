class Car():

    def __init__(self, make, model, year):
        '''инициализирует атрибуты описания автомобиля'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """возвращает аккуратно отформатированное описание"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """выводити пробег машины в милях"""
        print("Этот автомобиль имеет пробег " +
              str(self.odometer_reading) + " километров.")

    def update_odometer(self, milage):
        """при попытке обратной подкрутке изменение отклоняется"""
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("Вы не можете уменьшить показания спидометра!")

    def increment_odometer(self, miles):
        """увеличивает показания одометра с заданным приращением"""
        self.odometer_reading += miles


class Battery():
    """ простая модель аккумулятора электромобиля"""

    def __init__(self, battery_size=70):
        """инициализирует атрибуты аккумулятора"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о батарее"""
        print('Этот автомобиль имеет мощность батареи ' +
              str(self.battery_size) + ' кВт.')

    def get_range(self):
        """выводит приблизительный запас хода для аккумулятора"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 290
        message = "Этот авто может проехать примерно " + \
            str(range) + " км на полной зарядке аккумулятора."
        print(message)

    def upgrate_battery(self):
        """проверяет размер аккумулятора, если менне 85, то устанавливает это значение"""
        if self.battery_size < 85:
            self.battery_size = 85
        return self.battery_size


class ElectricCar(Car):
    """ представляет аспекты машины, специфияеские для электромобилей"""

    def __init__(self, make, model, year):
        """инициализирует атрибуты класса-родителя
        Затем иниц. атрибуты, специфические для электромобилей"""
        super().__init__(make, model, year)
        self.battery = Battery()
