import turtle
import random
import time

# Setup the screen
turtle.setup(800, 600)
turtle.bgcolor("white")

turtle.speed(0)
turtle.penup()
turtle.goto(-300, 200)
turtle.pendown()
turtle.forward(600)

turtle.penup()
turtle.goto(-300, -200)
turtle.pendown()
turtle.forward(600)

turtle.hideturtle()

# Create turtles
colors = ["red", "blue", "green", "yellow", "purple"]
turtles = []

for i in range(5):
    racer = turtle.Turtle()
    racer.shape("turtle")
    racer.color(colors[i])
    racer.penup()
    racer.goto(-300, 150 - (i * 75))
    turtles.append(racer)

def ai_move(turtle):
    return random.randint(1, 10)  # Simple AI chooses random speed

def race():
    winner = None
    while not winner:
        for racer in turtles:
            move = ai_move(racer)
            racer.forward(move)
            if racer.xcor() >= 300:
                winner = racer
                break
    print(f"The winner is {winner.color()[0]}!")
    turtle.done()

# Start the race
time.sleep(1)
race()
