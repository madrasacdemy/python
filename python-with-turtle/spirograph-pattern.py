import turtle
import math
import random

def draw_spirograph(radius, num_loops, color):
    turtle.color(color)
    turtle.speed(0)
    
    for i in range(num_loops):
        angle = i * (360 / num_loops)
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        
        turtle.penup()
        turtle.goto(x, y - radius)
        turtle.pendown()
        turtle.circle(radius)

# Setup the turtle screen
turtle.bgcolor("black")
turtle.pensize(2)
colors = ["red", "blue", "green", "yellow", "purple", "orange"]

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

# Draw multiple spirographs with different radii and colors
for i in range(6, 50, 6):
    draw_spirograph(i * 5, 36, random.choice(colors))

turtle.hideturtle()
turtle.done()