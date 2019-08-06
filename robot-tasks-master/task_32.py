#!/usr/bin/python3

from pyrob.api import *


def rise():
    bx = 0
    while not wall_is_above():
        move_up()
        if cell_is_filled():
            bx += 1
        else:
            fill_cell()

    while not wall_is_beneath():
        move_down()
    return bx


@task(delay=0.01)
def task_8_18():
    
    n = 0
    while not wall_is_on_the_right():
        if wall_is_above() and not cell_is_filled():
            fill_cell()
        else:
            n = n + rise()
        move_right()
    mov('ax', n)


if __name__ == '__main__':
    run_tasks()
