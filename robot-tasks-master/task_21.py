#!/usr/bin/python3

from pyrob.api import *


def down():
    move_down()


def up():
    move_up()


def left():
    move_left()


def right():
    move_right()


def down_cicle():
    down()
    while not wall_is_beneath():
        right()
        fill_cell()
        down()


def up_cicle():
    left()
    while not wall_is_on_the_left():
        up()
        fill_cell()
        left()


@task(delay=0.05)
def task_4_11():

    for i in range(7):
        i = down_cicle()
        i = up_cicle()
    right()


if __name__ == '__main__':
    run_tasks()
