#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    while not wall_is_on_the_right() and wall_is_above() and wall_is_beneath():
        move_right()
        while not wall_is_above() and wall_is_on_the_right():
            move_up()
            while not wall_is_on_the_left() and wall_is_above() and not wall_is_beneath():
                move_left()

    if wall_is_on_the_right() and wall_is_above() and wall_is_beneath():
        while not wall_is_on_the_left() and wall_is_above() and wall_is_beneath():
            move_left()
        while not wall_is_above() and wall_is_on_the_left():
            move_up()
        if wall_is_on_the_left() and wall_is_above() and wall_is_beneath():
            move_right(n=8)

        '''if wall_is_on_the_right() and wall_is_above():
            while not wall_is_on_the_left() and not wall_is_above():
                move_left()
            while not wall_is_above():
                move_up()'''


if __name__ == '__main__':
    run_tasks()
