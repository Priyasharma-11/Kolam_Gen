import turtle

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
t = turtle.Turtle()
t.speed(0)
sides = 10
layers = 10

for j in range(layers):
    t.pencolor(colors[j % len(colors)])
    for i in range(sides):
        t.forward(30 + j*3)
        t.right(360 / sides)
    t.right(360 / layers)

turtle.done()