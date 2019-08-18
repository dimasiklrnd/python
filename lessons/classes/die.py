from random import randint


class Die():
    """игральный кубик"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self, a, b):
        """иммтация броска кубика"""
        self.a=a
        self.b = b
        self.sides = randint(self.a, self.b)
        return self.sides
