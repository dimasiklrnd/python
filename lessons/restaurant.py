class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\nRestaurant name is " + self.restaurant_name.title() + '.')
        print("Restaurant type is " + self.cuisine_type.title() + '.')

    def open_restaurant(self):
        print(self.restaurant_name.title() + " now is opened.")
