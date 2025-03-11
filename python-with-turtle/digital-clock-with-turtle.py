import turtle
import time

def draw_clock():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Digital Clock")
    
    clock_turtle = turtle.Turtle()
    clock_turtle.hideturtle()
    clock_turtle.speed(0)
    clock_turtle.color("white")
    clock_turtle.penup()
    
    while True:
        clock_turtle.clear()
        current_time = time.strftime("%H:%M:%S")
        clock_turtle.goto(0, 0)
        clock_turtle.write(current_time, align="center", font=("Arial", 50, "bold"))
        time.sleep(1)

# Run the clock
draw_clock()