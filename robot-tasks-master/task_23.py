#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    while not wall_is_on_the_right():
        move_right()
        while not wall_is_above():
            move_up()
            fill_cell()
        while not wall_is_beneath() and wall_is_on_the_left() and wall_is_on_the_right():
            move_down()

    while not wall_is_on_the_left():
        move_left()
    move_right()


if __name__ == '__main__':
    run_tasks()
