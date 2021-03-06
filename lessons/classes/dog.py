class Dog():
    """Простая модель собаки"""

    def __init__(self, name, age):
        """инициализирует атрибуты name и age"""
        self.name = name
        self.age = age

    def sit(self):
        """собака садится по команде"""
        print(self.name.title() + ', сейчас сидит.')

    def roll_over(self):
        """собака перекатывается по команде"""
        print(self.name.title() + ', перевернулся.')
