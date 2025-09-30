import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.setup(width=700, height=700)  # Adjusted size for this design
screen.bgcolor("black")  # Assuming a dark background
screen.title("Elliptical Kolam Design")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0)  # Fastest speed
pen.color("white")
pen.pensize(2)
pen.penup()  # Start with pen up


# Function to draw a dot
def draw_dot(x, y, radius=5):
    pen.penup()
    pen.goto(x, y - radius)  # Adjust y to start drawing circle from bottom
    pen.pendown()
    pen.dot(radius * 2, "white")  # Use pen.dot for a filled circle


# Function to draw an ellipse
# This is a simplified approximation by drawing a circle and then manually
# adjusting `x` and `y` movement for elongation.
# A more common way in turtle is to draw many small segments.
# For a vertical ellipse at (x,y)
def draw_vertical_ellipse(center_x, center_y, major_axis, minor_axis):
    pen.penup()
    pen.goto(center_x, center_y - major_axis / 2)  # Start at bottom of ellipse
    pen.pendown()

    # We'll approximate an ellipse using many small steps
    steps = 90  # Number of segments to draw the ellipse
    angle_step = 360 / steps

    for i in range(steps + 1):
        angle_rad = math.radians(i * angle_step)
        x = center_x + (minor_axis / 2) * math.sin(angle_rad)
        y = center_y + (major_axis / 2) * math.cos(angle_rad)

        if i == 0:
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
        else:
            pen.goto(x, y)
    pen.penup()


# For a horizontal ellipse at (x,y)
def draw_horizontal_ellipse(center_x, center_y, major_axis, minor_axis):
    pen.penup()
    pen.goto(center_x - major_axis / 2, center_y)  # Start at left of ellipse
    pen.pendown()

    steps = 90  # Number of segments to draw the ellipse
    angle_step = 360 / steps

    for i in range(steps + 1):
        angle_rad = math.radians(i * angle_step)
        x = center_x + (major_axis / 2) * math.cos(angle_rad)
        y = center_y + (minor_axis / 2) * math.sin(angle_rad)

        if i == 0:
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
        else:
            pen.goto(x, y)
    pen.penup()


# --- Drawing the Kolam Design ---

# Parameters for the ellipses and spacing
ellipse_major_axis = 120  # Height of vertical ellipse / Width of horizontal ellipse
ellipse_minor_axis = 70  # Width of vertical ellipse / Height of horizontal ellipse
offset = 75  # Distance from center to the center of each ellipse

# 1. Central dot
draw_dot(0, 0, radius=7)

# 2. Four larger ellipses
# Top vertical ellipse
draw_vertical_ellipse(0, offset, ellipse_major_axis, ellipse_minor_axis)
# Bottom vertical ellipse
draw_vertical_ellipse(0, -offset, ellipse_major_axis, ellipse_minor_axis)
# Right horizontal ellipse
draw_horizontal_ellipse(offset, 0, ellipse_major_axis, ellipse_minor_axis)
# Left horizontal ellipse
draw_horizontal_ellipse(-offset, 0, ellipse_major_axis, ellipse_minor_axis)

# 3. Four outer dots
outer_dot_radius = 8
# Calculate positions for outer dots.
# These dots are roughly at the points where the ellipses' outer edges would be
# We can estimate their positions
outer_offset = offset + ellipse_major_axis / 2 - 20  # Adjust -20 for precise positioning

draw_dot(0, outer_offset, outer_dot_radius)  # Top outer dot
draw_dot(0, -outer_offset, outer_dot_radius)  # Bottom outer dot
draw_dot(outer_offset, 0, outer_dot_radius)  # Right outer dot
draw_dot(-outer_offset, 0, outer_dot_radius)  # Left outer dot

# Hide the turtle and display the result
pen.hideturtle()
turtle.done()