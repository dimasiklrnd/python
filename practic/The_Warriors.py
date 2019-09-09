class Warrior:
    def __init__(self, health=50, attack=5):
        self.h = health
        self.a = attack
        self.is_alive = True


class Knight(Warrior):
    def __init__(self, health=50, attack=7):
        self.a = attack
        self.h = health
        self.is_alive = True


def fight(unit_1, unit_2):

    while unit_1.h > 0 and unit_2.h > 0:
        unit_2.h -= unit_1.a
        print(unit_2.h)
        if unit_1.h > 0 and unit_2.h <= 0:
            unit_2.is_alive = False
            return True
        unit_1.h -= unit_2.a
        print(unit_1.h)

        if unit_2.h > 0 and unit_1.h <= 0:
            unit_1.is_alive = False
            return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    print(chuck.is_alive)
    bruce = Warrior()
    carl = Knight()
    print(carl.is_alive)
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
