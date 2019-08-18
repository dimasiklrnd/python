from dog import Dog

my_dog = Dog('lady', 5)
print("My dog is name " + my_dog.name.title() + '.')
print("My dog is " + str(my_dog.age) + " years old.\n")
my_dog.sit()
my_dog.roll_over()
