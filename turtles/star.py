import turtle as t

t.shape('turtle')


t.penup()
t.forward(150)
t.left(90)
t.forward(30)
t.pendown()
t.left(90)

def star(n, dlina):
	if n%2!=0:
		for i in range(n):
			t.forward(dlina)
			angle = n//2*360/n
			t.left(angle)


star(21, 300)
t.mainloop()
