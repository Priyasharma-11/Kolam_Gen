import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Make the turtle
t = turtle.Turtle()
t.speed(2)

# Draw dots (like a Kolam dot grid)
def draw_dots(rows, cols, spacing):
    for i in range(rows):
        for j in range(cols):
            t.penup()
            t.goto(j * spacing, -i * spacing)
            t.dot(5, "black")

# Draw a simple loop around a dot
def draw_loop_around_dot(x, y, size):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.forward(size)
    t.pendown()
    t.circle(size)

# Let's draw
draw_dots(3, 3, 40)

# Draw loops around each dot
for i in range(3):
    for j in range(3):
        draw_loop_around_dot(j * 40, -i * 40, 10)

t.hideturtle()
screen.mainloop()
