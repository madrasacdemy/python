import turtle

def draw_square(size):
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

def draw_circle(radius):
    turtle.circle(radius)

def draw_triangle(size):
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)

def draw_polygon(sides, length):
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(length)
        turtle.right(angle)

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("white")
turtle.speed(3)

# Draw shapes
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()
draw_square(100)

turtle.penup()
turtle.goto(100, 100)
turtle.pendown()
draw_circle(50)

turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()
draw_triangle(100)

turtle.penup()
turtle.goto(100, -100)
turtle.pendown()
draw_polygon(6, 60)  # Hexagon

turtle.hideturtle()
turtle.done()
