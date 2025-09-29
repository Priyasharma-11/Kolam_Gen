import turtle as t

t.speed(0)
t.bgcolor("black")
t.pencolor("white")

# Draw grid of dots
for y in range(-150, 200, 50):
    for x in range(-150, 200, 50):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(8, "white")

t.hideturtle()
t.done()