import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black") # Assuming a dark background like in the image
screen.title("Kolam Design")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0) # Fastest speed
pen.color("white") # Kolam is white
pen.pensize(2)

# Function to draw a circle
def draw_circle(radius, x, y):
    pen.penup()
    pen.goto(x, y - radius) # Adjust y to start drawing circle from bottom
    pen.pendown()
    pen.circle(radius)

# Function to draw a dot (small filled circle)
def draw_dot(radius, x, y):
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

# --- Drawing the main design ---

# Outer large circle
outer_radius = 150
draw_circle(outer_radius, 0, 0)

# Main cross lines
pen.penup()
pen.goto(-outer_radius, 0)
pen.pendown()
pen.goto(outer_radius, 0)

pen.penup()
pen.goto(0, -outer_radius)
pen.pendown()
pen.goto(0, outer_radius)

# Dots on the outer circle's intersection points
dot_radius = 8
draw_dot(dot_radius, 0, outer_radius)   # Top dot
draw_dot(dot_radius, 0, -outer_radius)  # Bottom dot
draw_dot(dot_radius, outer_radius, 0)   # Right dot
draw_dot(dot_radius, -outer_radius, 0)  # Left dot

# Inner square/diamond and circles
inner_offset = 70 # Adjust this value to change the size of the inner diamond and circles
inner_circle_radius = 25

# Draw the inner diamond (square rotated by 45 degrees)
pen.penup()
pen.goto(0, inner_offset)
pen.pendown()
pen.goto(inner_offset, 0)
pen.goto(0, -inner_offset)
pen.goto(-inner_offset, 0)
pen.goto(0, inner_offset) # Complete the diamond

# Draw the four inner circles
draw_circle(inner_circle_radius, 0, inner_offset)   # Top inner circle
draw_circle(inner_circle_radius, 0, -inner_offset)  # Bottom inner circle
draw_circle(inner_circle_radius, inner_offset, 0)   # Right inner circle
draw_circle(inner_circle_radius, -inner_offset, 0)  # Left inner circle

# Hide the turtle and display the result
pen.hideturtle()
turtle.done()