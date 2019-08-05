#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    for i in range(6):
        i = cicle()

    move_right()


def cicle_right():
    while not wall_is_on_the_right():
        move_right()
        while not wall_is_on_the_right():
            fill_cell()
            move_right()


def down():
    move_down()


def cicle_left():
    while not wall_is_on_the_left():
        move_left()
        while not wall_is_on_the_left():
            fill_cell()
            move_left()


def cicle():
    cicle_right()
    down()
    cicle_left()
    down()


if __name__ == '__main__':
    run_tasks()
