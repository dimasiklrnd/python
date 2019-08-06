#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    n = 0
    while not cell_is_filled() and not wall_is_on_the_right() and n < 3:
        move_right()
        n = 0
        if n < 3 and cell_is_filled() and not wall_is_on_the_right():
            n += 1
            move_right()
            if n < 3 and cell_is_filled() and not wall_is_on_the_right():
                n += 1
                move_right()
                if n < 3 and cell_is_filled():
                    n += 1000


if __name__ == '__main__':
    run_tasks()
