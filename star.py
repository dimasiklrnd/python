import turtle as t

t.shape('turtle')

c=144
r = 200

t.penup()
t.forward(100)
t.left(90)
t.forward(30)
t.pendown()
t.left(90)

for i in range(4):
	t.forward(r)
	t.left(c)
t.forward(r)

t.mainloop()
