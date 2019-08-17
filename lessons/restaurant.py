class Restaurant():
    """Класс ресторан"""

    def __init__(self, restaurant_name, cuisine_type):
        """инициализация атрибутов"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """описывает название и тип заведения"""
        print("\nRestaurant name is " + self.restaurant_name.title() + '.')
        print("Restaurant type is " + self.cuisine_type.title() + '.')

    def open_restaurant(self):
        """выводит сообщение о том что ресторан открыт"""
        print(self.restaurant_name.title() + " now is opened.")

    def closed_restaurant(self):
        """ресторан закрыт"""
        print(self.restaurant_name.title() + " now is closed.")
