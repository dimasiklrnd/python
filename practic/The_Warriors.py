class Warrior:
    def __init__(self):
        self.h = 50
        self.a = 5
        self.is_alive = True


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.a = 7


def fight(unit_1, unit_2):

    while unit_1.h > 0 and unit_2.h > 0:

        unit_2.h -= unit_1.a
        if unit_1.h > 0 and unit_2.h <= 0:
            unit_2.is_alive = False
            return True

        unit_1.h -= unit_2.a
        if unit_2.h > 0 and unit_1.h <= 0:
            unit_1.is_alive = False
            return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
