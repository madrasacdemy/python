import turtle
import random
import time

def draw_star(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

def twinkling_stars():
    turtle.bgcolor("black")
    turtle.speed(0)
    turtle.hideturtle()
    
    stars = []
    colors = ["white", "yellow", "lightblue"]
    
    for _ in range(50):  # Generate random stars
        x = random.randint(-300, 300)
        y = random.randint(-250, 250)
        size = random.randint(5, 15)
        color = random.choice(colors)
        stars.append((x, y, size, color))
    
    while True:
        for star in stars:
            draw_star(star[0], star[1], star[2], random.choice(colors))
        time.sleep(0.5)
        turtle.clear()

# Run the twinkling stars animation
twinkling_stars()
