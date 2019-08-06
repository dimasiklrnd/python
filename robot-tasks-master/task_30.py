#!/usr/bin/python3

from pyrob.api import *


def rd():
    move_right()
    move_down()


# пробег по кругу
def around():
    counterWidth = 1  # счетчик. Узнаем длинну поля
    while not wall_is_on_the_right():
        move_right()
        counterWidth += 1
        if not wall_is_on_the_right():
            fill_cell()

    while not wall_is_beneath():
        move_down()
        if not wall_is_beneath():
            fill_cell()

    while not wall_is_on_the_left():
        move_left()
        if not wall_is_on_the_left():
            fill_cell()

    while not wall_is_above():
        move_up()
        if not wall_is_above():
            fill_cell()

    rd()
    n = 2
    width = (counterWidth//2)-1
    while width > 0:
        r = n
        while counterWidth-r > r:
            move_right()
            fill_cell()
            r += 1
        move_right()
        d = n
        while counterWidth-d > d:
            move_down()
            fill_cell()
            d += 1
        l = n
        move_down()

        while counterWidth-l > l:
            move_left()
            fill_cell()
            l += 1

        move_left()
        u = n
        while counterWidth-u > u:
            move_up()
            fill_cell()
            u += 1

        move_up()

    width -= 1
    n += 1

    """while not wall_is_on_the_left():
        move_left()
        while not wall_is_beneath():
            move_down()"""


@task(delay=0.01)
def task_9_3():
    around()


if __name__ == '__main__':
    run_tasks()
