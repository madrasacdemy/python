import turtle
import math
import time

# Create the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Spinning 3D Cube")

# Create the turtle
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.color("cyan")

# Function to draw a line between two 3D points projected into 2D
def draw_line(p1, p2):
    pen.penup()
    pen.goto(p1[0], p1[1])
    pen.pendown()
    pen.goto(p2[0], p2[1])

# Function to project 3D points into 2D
def project_3d(x, y, z, angle):
    # Simulate 3D rotation around the Y-axis
    new_x = x * math.cos(angle) - z * math.sin(angle)
    new_z = x * math.sin(angle) + z * math.cos(angle)
    # Perspective projection: shrink based on distance from the viewer
    factor = 200 / (new_z + 300)  # Adjust perspective factor for better effect
    proj_x = new_x * factor
    proj_y = y * factor
    return (proj_x, proj_y)

# Cube coordinates (relative to center)
cube_vertices = [
    (-50, -50, -50), (50, -50, -50), (50, 50, -50), (-50, 50, -50),  # Back face
    (-50, -50, 50), (50, -50, 50), (50, 50, 50), (-50, 50, 50)       # Front face
]

# Cube edges connecting the vertices
cube_edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Back face edges
    (4, 5), (5, 6), (6, 7), (7, 4),  # Front face edges
    (0, 4), (1, 5), (2, 6), (3, 7)   # Connecting edges between front and back faces
]

# Rotation angle
angle = 0

# Main loop to animate the spinning cube
while True:
    pen.clear()  # Clear the screen for each frame

    # Project all vertices
    projected_points = [project_3d(x, y, z, angle) for (x, y, z) in cube_vertices]

    # Draw all cube edges
    for edge in cube_edges:
        p1 = projected_points[edge[0]]
        p2 = projected_points[edge[1]]
        draw_line(p1, p2)

    # Increment the rotation angle to simulate spinning
    angle += 0.02
    time.sleep(0.02)  # Add a slight delay to control the animation speed

# Keep the window open
screen.mainloop()
