#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():

    width = 1
    while not wall_is_on_the_left():
        move_left()
        width += 1
    width_max = width

    while wall_is_beneath() and width > 1:
        move_right()
        width -= 1

    while not wall_is_beneath():
        move_down()
        if wall_is_beneath() and width > 1:
            while width > 1 and wall_is_beneath():
                move_right()
                width -= 1
            if wall_is_on_the_right():
                while width < width_max and wall_is_beneath():
                    move_left()
                    width += 1


if __name__ == '__main__':
    run_tasks()
