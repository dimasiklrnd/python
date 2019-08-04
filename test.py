import turtle

turtle.shape('turtle')

x = 3


def agles(x):
    a = 360/x
    while x > 0:
        turtle.left(a)
        turtle.forward(50)
        x -= 1


def position_turtle():
    turtle.penup()
    turtle.right(180)
    turtle.forward(15)
    turtle.left(180)
    turtle.pendown()


while x < 12:
    agles(x)
    position_turtle()
    x += 1
