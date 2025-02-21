import turtle
import random

# Setup screen
screen = turtle.Screen()
screen.title("Turtle Racing Game")
screen.bgcolor("lightgreen")

# Finish line
finish_line = 300

# Colors and turtle names
colors = ["red", "blue", "green", "orange", "purple", "yellow"]
turtles = []

# Create turtles and place them at the starting position
for i, color in enumerate(colors):
    racer = turtle.Turtle()
    racer.color(color)
    racer.shape("turtle")
    racer.penup()
    racer.goto(-300, 150 - i * 50)  # Position turtles with space between
    turtles.append(racer)

# Draw the finish line
line = turtle.Turtle()
line.hideturtle()
line.penup()
line.goto(finish_line, 200)
line.pendown()
line.right(90)
line.forward(400)

# Start the race
race_on = True
while race_on:
    for racer in turtles:
        # Move each turtle a random distance
        distance = random.randint(1, 10)
        racer.forward(distance)
        
        # Check if a turtle crosses the finish line
        if racer.xcor() >= finish_line:
            race_on = False
            winning_color = racer.color()[0]
            print(f"The winner is the {winning_color} turtle!")
            break

# Keep the window open
screen.mainloop()
