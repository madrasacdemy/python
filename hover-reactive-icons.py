import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")

# Create icon turtles
icons = []
num_icons = 10  # Number of interactive icons

for _ in range(num_icons):
    icon = turtle.Turtle()
    icon.shape("circle")
    icon.color("white")
    icon.penup()
    icon.goto(random.randint(-250, 250), random.randint(-250, 250))
    icon.shapesize(2)  # Default size
    icons.append(icon)

# Hover effect function
def on_hover(x, y):
    for icon in icons:
        if icon.distance(x, y) < 30:  # If mouse is near an icon
            icon.color(random.choice(["red", "blue", "green", "yellow", "purple", "cyan"]))
            icon.shapesize(3)  # Increase size
        else:
            icon.color("white")
            icon.shapesize(2)  # Reset size

# Track mouse movement
screen.listen()
screen.onscreenclick(on_hover)  # Detect mouse hover

# Keep window open
screen.mainloop()
