import turtle


def draw_kolam(rows=5, cols=5, cell_size=40):
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    start_x = -cols * cell_size // 2
    start_y = rows * cell_size // 2

    for r in range(rows):
        for c in range(cols):
            x = start_x + c * cell_size
            y = start_y - r * cell_size
            t.penup()
            t.goto(x, y)
            t.pendown()
            # Draw a simple dot pattern mimicking Kolam dots
            t.dot(10, "black")

            # Draw cross '/' and '\' lines intersecting the dot
            t.penup()
            t.goto(x - 10, y + 10)
            t.pendown()
            t.goto(x + 10, y - 10)

            t.penup()
            t.goto(x - 10, y - 10)
            t.pendown()
            t.goto(x + 10, y + 10)

    screen.mainloop()


# Example usage
draw_kolam()
