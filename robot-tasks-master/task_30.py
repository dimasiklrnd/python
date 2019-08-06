#!/usr/bin/python3

from pyrob.api import *


def rd():
    move_right()
    move_down()


@task(delay=0.01)
def task_9_3():

    # first around
    counterWidth = 1
    while not wall_is_on_the_right():
        move_right()
        counterWidth += 1  # счетчик. Узнаем длинну поля
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

# other around
    n = 2  # отступ справа второго круга, т.к. этот цикл начинаем с него
    width = (counterWidth//2)-1  # количество оборотов

    while width > 0:

        r = n
        r1 = (counterWidth-r)
        while r1 > r:
            move_right()
            fill_cell()
            r += 1
        move_right()

        d = n
        d1 = (counterWidth-d)
        while d1 > d:
            move_down()
            fill_cell()
            d += 1
        move_down()

        l = n
        l1 = (counterWidth-l)
        while l1 > l:
            move_left()
            fill_cell()
            l += 1
        move_left()

        u = n
        u1 = (counterWidth-u)
        while u1 > u:
            move_up()
            fill_cell()
            u += 1
        move_up()

        width -= 1
        n += 1
        rd()

# уходим в левый нижний угол
    while not wall_is_on_the_left():
        move_left()
        while not wall_is_beneath():
            move_down()


if __name__ == '__main__':
    run_tasks()
