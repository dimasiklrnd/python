import turtle

''' #10 вложенных квадратов

x = 10
n = 10
while x >= 0:
	turtle.pendown()
	turtle.shape('turtle')
	turtle.color('red')
	turtle.forward(n)
	turtle.left(90)
	turtle.forward(n)
	turtle.left(90)
	turtle.forward(n)
	turtle.left(90)
	turtle.forward(n)
	turtle.penup()
	turtle.forward(5)
	turtle.right(90)
	turtle.forward(5)
	turtle.left(180)

	x = x - 1
	n = n + 10 '''


'''#Круг (можно просчитать как остановилась в конце)
	turtle.shape('turtle')
	while True:
		turtle.forward(1)
		turtle.left(1)
	'''


'''#Паук
x = 11
n = 80


turtle.shape('turtle')
turtle.color('green')
while x >= 0:
	turtle.pendown()
	turtle.forward(n)
	turtle.stamp()
	turtle.penup()
	turtle.backward(n)
	turtle.right(30)
	x = x - 1'''

'''#Спираль
turtle.shape('turtle')
n=0.2
while n<5:

	turtle.forward(n)
	turtle.left(6)
	n+=0.01'''

# Квадратная спираль
turtle.shape('turtle')
n = 5
while n < 200:

    turtle.forward(n)
    turtle.left(90)
    n += 5
