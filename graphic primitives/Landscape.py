import graphics as gr

w = 800
h = 600

window = gr.GraphWin("Landscape", w, h)


# фон неба
sky = gr.Rectangle(gr.Point(0, 0), gr.Point(w, h/2))
sky.setFill('blue')

# фон земли
land = gr.Rectangle(gr.Point(0, h/2), gr.Point(w, h))
land.setFill('lightgray')

# окно в доме
wind = gr.Rectangle(gr.Point(w/3-40, h/2-40), gr.Point(w/3+40, h/2+40))
wind.setFill('yellow')
wind.setWidth(5)

# решетки окна
wind_line1 = gr.Line(gr.Point(w/3, h/2-40),
                     gr.Point(w/3, h/2+40))
wind_line2 = gr.Line(gr.Point(w/3-40, h/2),
                     gr.Point(w/3+40, h/2))
wind_line1.setWidth(5)
wind_line2.setWidth(5)

# стены дома
building = gr.Rectangle(gr.Point(w/3-100, h/2-100), gr.Point(w/3+100, h/2+100))
building.setFill('gray')
building.setWidth(5)

# крыша дома
roof = gr.Polygon(gr.Point(w/3-100, h/2-100), gr.Point(w /
                                                       3, h/2-200), gr.Point(w/3+100, h/2-100))
roof.setFill('darkred')
roof.setWidth(5)

# облака
cloud = gr.Circle(gr.Point(w/10, h/10), 20)
cloud.setFill('white')
j = w
j += 200
k = h
cloud1 = gr.Circle(gr.Point(j/10, k/10), 20)
cloud1.setFill('white')
k += 100
j += 100
cloud2 = gr.Circle(gr.Point(j/10, k/10), 20)
cloud2.setFill('white')
j -= 200
cloud3 = gr.Circle(gr.Point(j/10, k/10), 20)
cloud3.setFill('white')
j -= 200
cloud4 = gr.Circle(gr.Point(j/10, k/10), 20)
cloud4.setFill('white')

# луна
moon = gr.Circle(gr.Point(w/1.4, h/7), 50)
moon.setFill('yellow')


# ветви елки
p = h
tree = gr.Polygon(gr.Point(w/1.4-50, h/2+70), gr.Point(w /
                                                       1.4+40, h/2-30), gr.Point(w/1.4+120, h/2+70))
tree.setFill('darkgreen')
tree.setWidth(5)
p += 100
tree1 = gr.Polygon(gr.Point(w/1.4-50, p/2+70), gr.Point(w /
                                                        1.4+40, p/2-30), gr.Point(w/1.4+120, p/2+70))
tree1.setFill('darkgreen')
tree1.setWidth(5)
p += 100
tree2 = gr.Polygon(gr.Point(w/1.4-50, p/2+70), gr.Point(w /
                                                        1.4+40, p/2-30), gr.Point(w/1.4+120, p/2+70))
tree2.setFill('darkgreen')
tree2.setWidth(5)

# ствол дерева
trunk = gr.Rectangle(gr.Point(w/1.4+32, p/2+70), gr.Point(w/1.4+48, p/2+170))
trunk.setFill('brown')
trunk.setWidth(5)


# далее вызываем наши объекты на рисование в той последовательности,
# при которой слои соответственно будут накладываться друг на друга
sky.draw(window)
land.draw(window)

cloud.draw(window)
cloud1.draw(window)
cloud2.draw(window)
cloud3.draw(window)
cloud4.draw(window)

moon.draw(window)
building.draw(window)
wind.draw(window)
roof.draw(window)
wind_line1.draw(window)
wind_line2.draw(window)
tree2.draw(window)
tree1.draw(window)
tree.draw(window)
trunk.draw(window)


window.getMouse()

#  После того как мы выполнили все нужные операции, окно следует закрыть.
window.close()
