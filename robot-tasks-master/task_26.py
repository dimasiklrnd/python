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


@task(delay=0.02)
def task_2_4():
    i = 9
    while i > 0:
        make_cross()
        move_right(n=4)
        i -= 1

    make_cross()


if __name__ == '__main__':
    run_tasks()
