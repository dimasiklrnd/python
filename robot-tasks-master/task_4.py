#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    if wall_is_on_the_right() and wall_is_above() and wall_is_beneath():
        move_left()
    elif wall_is_on_the_right() and wall_is_above() and wall_is_on_the_left():
        move_down()
    elif wall_is_beneath() and wall_is_above() and wall_is_on_the_left():
        move_right()
    else:
        move_up()


if __name__ == '__main__':
    run_tasks()
