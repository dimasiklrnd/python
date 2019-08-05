#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():

    move_right()
    fill_cell()

    n = m = 0

    while not wall_is_on_the_right():
        if n < m:
            n += 1
            move_right()
        else:
            n = 0
            m += 1
            move_right()
            fill_cell()


if __name__ == '__main__':
    run_tasks()
