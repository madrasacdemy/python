import turtle

def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_chakra():
    turtle.penup()
    turtle.goto(0, -20)
    turtle.pendown()
    turtle.color("navy")
    turtle.width(2)
    turtle.circle(30)
    
    # Draw 24 spokes
    for _ in range(24):
        turtle.penup()
        turtle.goto(0, 13)
        turtle.pendown()
        turtle.forward(30)
        turtle.backward(30)
        turtle.right(15)

def draw_indian_flag():
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Indian Flag")
    turtle.speed(3)
    
    # Draw Saffron Rectangle
    draw_rectangle("orange", -180, 100, 360, 60)
    
    # Draw White Rectangle
    draw_rectangle("white", -180, 40, 360, 60)
    
    # Draw Green Rectangle
    draw_rectangle("green", -180, -20, 360, 60)
    
    # Draw Ashoka Chakra
    draw_chakra()
    
    # Hide Turtle
    turtle.hideturtle()
    turtle.done()

# Run the function
draw_indian_flag()