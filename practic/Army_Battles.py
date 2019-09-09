'''В прошлой миссии — Warriors — вы научились устраивать дуэли между 2 отдельными воинами. Отличная работа! Но давайте перейдём к чему-то более эпичному — к армиям! В этой миссии ваша задача — добавить к уже существующим классам и функциям новые: Army, который будет обладать методом add_units(), позволяющим добавлять выбранное количество воинов в армию, а также класс Battle() с функцией fight(), которая будет устраивать сражения и определять сильнейшую армию.
Сражения между армиями происходят по следующему принципу:
• сперва проводится дуэль между первым воином первой армии и первым воином второй
• как только один из них погибает — в дуэль вступает следующий воин из той армии, которая потеряла бойца, а выживший воин со своим текущим здоровьем продолжает сражаться
• так продолжается до тех пор, пока все воины одной из армий не умрут. В этом случае функция battle() возвращает True, если первая армия выиграла или False,если вторая оказалась сильнее.

Пример:
chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()

fight(chuck, bruce) == True
fight(dave, carl) == False
chuck.is_alive == True
bruce.is_alive == False
carl.is_alive == True
dave.is_alive == False
fight(carl, mark) == False
carl.is_alive == False

my_army = Army()
my_army.add_units(Knight, 3)

enemy_army = Army()
enemy_army.add_units(Warrior, 3)

army_3 = Army()
army_3.add_units(Warrior, 20)
army_3.add_units(Knight, 5)

army_4 = Army()
army_4.add_units(Warrior, 30)

battle = Battle()

battle.fight(my_army, enemy_army) == True
battle.fight(army_3, army_4) == False

Входные данные: воины и армии.
Выходные данные: результат битвы (True или False).

Предусловие: 2 типа солдат
'''

# Taken from mission The Warriors

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
    #These "asserts" using only for self-checking and not necessary for auto-testing

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


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    #fight tests
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

    #battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")