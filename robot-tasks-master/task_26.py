#!/usr/bin/python3

from pyrob.api import *


def make_cross():
    move_right()
    fill_cell()
    move_down()
    fill_cell()
    move_right()
    fill_cell()
    move_left()
    move_down()
    fill_cell()
    move_up()
    move_left()
    fill_cell()
    move_up()


def prohod_right():
    i = 9
    while i > 0:
        make_cross()
        move_right(n=4)
        i -= 1
    make_cross()


def prohod_left():
    move_down(n=4)
    i = 9
    while i > 0:
        make_cross()
        move_left(n=4)
        i -= 1
    make_cross()


@task(delay=0.02)
def task_2_4():

    for i in range(2):
        i = prohod_right()
        i = prohod_left()
        i = move_down(n=4)

    prohod_right()

    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()
