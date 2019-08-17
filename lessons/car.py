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
        print("This car has " + str(self.odometer_reading) + " kilometers on it.")

    def update_odometer(self, milage):
        """при попытке обратной подкрутке изменение отклоняется"""
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """увеличивает показания одометра с заданным приращением"""
        self.odometer_reading += miles

