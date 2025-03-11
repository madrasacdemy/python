import turtle
import random

def draw_spiral():
    screen = turtle.Screen()
    screen.bgcolor("black")
    turtle.speed(0)
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "cyan", "white"]
    
    for i in range(100):
        turtle.pencolor(random.choice(colors))
        turtle.forward(i * 2)
        turtle.right(59)
        turtle.width(i / 50 + 1)
    
    turtle.hideturtle()
    turtle.done()

# Run the function
draw_spiral()