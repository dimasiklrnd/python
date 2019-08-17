class Restaurant():
    """Класс ресторан"""

    def __init__(self, restaurant_name, cuisine_type, обслуж_клиенты=0):
        """инициализация атрибутов"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.обслуж_клиенты = обслуж_клиенты

    def describe_restaurant(self):
        """описывает название и тип заведения"""
        print("\nRestaurant name is " + self.restaurant_name.title() + '.')
        print("Restaurant type is " + self.cuisine_type.title() + '.')

    def open_restaurant(self):
        """выводит сообщение о том что ресторан открыт"""
        print(self.restaurant_name.title() + " now is opened.")
        print("Обслужено клиентов сегодня: " + str(self.обслуж_клиенты))

    def closed_restaurant(self):
        """ресторан закрыт"""
        print(self.restaurant_name.title() + " now is closed.")
        print("Обслужено клиентов сегодня: " + str(self.обслуж_клиенты))
