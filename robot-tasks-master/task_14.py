#!/usr/bin/python3

from pyrob.api import *


def wall():
    if wall_is_above() and wall_is_beneath():
        fill_cell()
    elif not wall_is_above() and wall_is_beneath():
        move_up()
        fill_cell()
        move_down()
    elif wall_is_above() and not wall_is_beneath():
        move_down()
        fill_cell()
        move_up()
    elif not wall_is_above() and not wall_is_beneath():
        move_down()
        fill_cell()
        move_up()
        move_up()
        fill_cell()
        move_down()


@task
def task_8_11():
    while not wall_is_on_the_right():
        wall()
        move_right()
    wall()


if __name__ == '__main__':
    run_tasks()
