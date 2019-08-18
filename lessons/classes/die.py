from random import randint


class Die():
    """игральный кубик"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """иммтация броска кубика"""
        self.sides = randint(1, 6)
        return self.sides
