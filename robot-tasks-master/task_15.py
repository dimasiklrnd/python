#!/usr/bin/python3

from pyrob.api import *


def wall():
    if wall_is_above() and wall_is_on_the_left():
        while not wall_is_beneath() and not wall_is_on_the_right():
            move_right(n=1)
            move_down(n=1)
    elif wall_is_above() and wall_is_on_the_right():
        while not wall_is_beneath() and not wall_is_on_the_left():
            move_left(n=1)
            move_down(n=1)
    elif wall_is_beneath() and wall_is_on_the_right():
        while not wall_is_above() and not wall_is_on_the_left():
            move_left(n=1)
            move_up(n=1)
    elif wall_is_beneath() and wall_is_on_the_left():
        while not wall_is_above() and not wall_is_on_the_right():
            move_right(n=1)
            move_up(n=1)


@task
def task_8_21():
    wall()


if __name__ == '__main__':
    run_tasks()
