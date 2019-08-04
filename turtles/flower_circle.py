import turtle as t

t.shape('turtle')


def circle_1(d1):

    while d1 > 0:
        t.forward(0.5)
        t.left(1)
        d1 -= 1


def circle_2(d2):

    while d2 > 0:
        t.forward(0.5)
        t.right(1)
        d2 -= 1
    t.left(60)


i = 0
while i < 3:
    circle_1(360)
    circle_2(360)
    i += 1
t.mainloop()
