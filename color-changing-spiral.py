import turtle
import colorsys

# Create screen and turtle
screen = turtle.Screen()
screen.bgcolor("black")
spiral = turtle.Turtle()
spiral.speed(0)  # Set the fastest speed

# Initial values
hue = 0.0  # Hue value for the color (HSV model)

# Draw the color-changing spiral
for i in range(360):
    # Convert hue to RGB
    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    spiral.color(color)  # Set the color of the turtle
    
    # Draw the spiral
    spiral.forward(i * 2)
    spiral.left(59)  # Angle to create the spiral effect
    
    # Increment hue to change color
    hue += 0.01
    if hue > 1.0:
        hue = 0.0  # Reset hue if it exceeds 1.0

# Finish drawing
spiral.hideturtle()
turtle.done()
