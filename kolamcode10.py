import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.setup(width=700, height=700)  # Adjusted size for this design
screen.bgcolor("black")  # Assuming a dark background
screen.title("Layered Kolam Design")

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
    pen.penup()


# Function to draw a square given its center and side length
def draw_square(center_x, center_y, side_length):
    half_side = side_length / 2
    pen.penup()
    pen.goto(center_x - half_side, center_y + half_side)  # Top-left corner
    pen.pendown()
    pen.goto(center_x + half_side, center_y + half_side)  # Top-right
    pen.goto(center_x + half_side, center_y - half_side)  # Bottom-right
    pen.goto(center_x - half_side, center_y - half_side)  # Bottom-left
    pen.goto(center_x - half_side, center_y + half_side)  # Close square
    pen.penup()


# Function to draw a diamond (rotated square) given its center and the distance from center to a corner
def draw_diamond(center_x, center_y, distance_to_corner):
    pen.penup()
    pen.goto(center_x, center_y + distance_to_corner)  # Top corner
    pen.pendown()
    pen.goto(center_x + distance_to_corner, center_y)  # Right corner
    pen.goto(center_x, center_y - distance_to_corner)  # Bottom corner
    pen.goto(center_x - distance_to_corner, center_y)  # Left corner
    pen.goto(center_x, center_y + distance_to_corner)  # Close diamond
    pen.penup()


# Function to draw a circle given its center and radius
def draw_circle(center_x, center_y, radius):
    pen.penup()
    pen.goto(center_x, center_y - radius)  # Start at bottom of circle
    pen.pendown()
    pen.circle(radius)
    pen.penup()


# Function to draw an ellipse (approximation) for the central clover
# This is a simplified approximation using many small steps
def draw_ellipse(center_x, center_y, major_axis, minor_axis, rotation_angle=0):
    pen.penup()

    steps = 90  # Number of segments to draw the ellipse
    angle_step = 360 / steps

    for i in range(steps + 1):
        angle_rad = math.radians(i * angle_step)

        # Ellipse point relative to its center
        x_rel = (major_axis / 2) * math.cos(angle_rad)
        y_rel = (minor_axis / 2) * math.sin(angle_rad)

        # Apply rotation (if any)
        rotated_x_rel = x_rel * math.cos(math.radians(rotation_angle)) - y_rel * math.sin(math.radians(rotation_angle))
        rotated_y_rel = x_rel * math.sin(math.radians(rotation_angle)) + y_rel * math.cos(math.radians(rotation_angle))

        # Absolute position
        x = center_x + rotated_x_rel
        y = center_y + rotated_y_rel

        if i == 0:
            pen.goto(x, y)
            pen.pendown()
        else:
            pen.goto(x, y)
    pen.penup()


# --- Drawing the Kolam Design ---

# Parameters
outer_square_side = 300
dot_radius = 6

# 1. Outer Square
draw_square(0, 0, outer_square_side)

# 2. Dots at outer square corners
half_side = outer_square_side / 2
draw_dot(half_side, half_side, dot_radius)  # Top-right
draw_dot(-half_side, half_side, dot_radius)  # Top-left
draw_dot(half_side, -half_side, dot_radius)  # Bottom-right
draw_dot(-half_side, -half_side, dot_radius)  # Bottom-left

# 3. Inner Diamond (rotated square)
# The distance from center to corner of this diamond is half_side
diamond_corner_dist = half_side
draw_diamond(0, 0, diamond_corner_dist)

# 4. Dots at midpoints of outer square sides (corners of inner diamond)
draw_dot(0, half_side, dot_radius)  # Top
draw_dot(0, -half_side, dot_radius)  # Bottom
draw_dot(half_side, 0, dot_radius)  # Right
draw_dot(-half_side, 0, dot_radius)  # Left

# 5. Large Circle
# The radius of this circle is the distance from the center to the midpoints of the diamond's sides
# Which is diamond_corner_dist / sqrt(2) or half_side / sqrt(2)
large_circle_radius = diamond_corner_dist / math.sqrt(2)
draw_circle(0, 0, large_circle_radius)

# 6. Dots where the large circle touches the inner diamond
# These points are at (r_circle, 0), (-r_circle, 0), (0, r_circle), (0, -r_circle) for the large circle
draw_dot(large_circle_radius, 0, dot_radius)
draw_dot(-large_circle_radius, 0, dot_radius)
draw_dot(0, large_circle_radius, dot_radius)
draw_dot(0, -large_circle_radius, dot_radius)

# 7. Central "Clover" Pattern (four small ellipses)
# Parameters for the small ellipses
small_ellipse_major_axis = 40
small_ellipse_minor_axis = 20
small_ellipse_offset = 20  # Distance from center to center of small ellipse
small_dot_radius = 4

# Central small dot for the clover
draw_dot(0, 0, small_dot_radius)

# Four small ellipses
draw_ellipse(0, small_ellipse_offset, small_ellipse_major_axis, small_ellipse_minor_axis,
             rotation_angle=90)  # Top (vertical)
draw_ellipse(0, -small_ellipse_offset, small_ellipse_major_axis, small_ellipse_minor_axis,
             rotation_angle=90)  # Bottom (vertical)
draw_ellipse(small_ellipse_offset, 0, small_ellipse_major_axis, small_ellipse_minor_axis,
             rotation_angle=0)  # Right (horizontal)
draw_ellipse(-small_ellipse_offset, 0, small_ellipse_major_axis, small_ellipse_minor_axis,
             rotation_angle=0)  # Left (horizontal)

# 8. Small dots around the central clover
# These are at the "outer" ends of the clover's ellipses
clover_outer_dot_offset = small_ellipse_offset + small_ellipse_major_axis / 2
draw_dot(0, clover_outer_dot_offset, small_dot_radius)
draw_dot(0, -clover_outer_dot_offset, small_dot_radius)
draw_dot(clover_outer_dot_offset, 0, small_dot_radius)
draw_dot(-clover_outer_dot_offset, 0, small_dot_radius)

# Hide the turtle and display the result
pen.hideturtle()
turtle.done()