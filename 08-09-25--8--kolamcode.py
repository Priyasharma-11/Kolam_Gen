import turtle

t = turtle.Turtle()
t.speed(0)
dot_distance = 40
n = 5  # 5x5 grid

# draw dots grid
for y in range(n):
    for x in range(n):
        t.penup()
        t.goto(x*dot_distance, y*dot_distance)
        t.pendown()
        t.dot(6, "black")

# connect center dots for star
for i in range(n-1):
    t.penup()
    t.goto(dot_distance, (i+1)*dot_distance)
    t.pendown()
    t.goto((n-2)*dot_distance, (i+1)*dot_distance)
    t.penup()

turtle.done()