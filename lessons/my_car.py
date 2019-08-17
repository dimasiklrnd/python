from car import Car

my_new_car=Car('nissan', 'almera classic', '2009')
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading=193456
my_new_car.increment_odometer(1235)
my_new_car.update_odometer(678)# не удасться открутить назад
my_new_car.read_odometer()