import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fireworks Animation")

# Create the turtle
firework = turtle.Turtle()
firework.hideturtle()
firework.speed(0)  # Fastest speed

# Function to draw a single firework burst
def draw_firework(x, y):
    firework.penup()
    firework.goto(x, y)
    firework.pendown()

    # Random burst size and number of particles
    num_particles = random.randint(20, 50)
    burst_size = random.randint(50, 150)

    # Random color for each burst
    color = (random.random(), random.random(), random.random())
    firework.color(color)

    for _ in range(num_particles):
        angle = random.uniform(0, 360)
        distance = random.uniform(20, burst_size)
        
        firework.penup()
        firework.goto(x, y)
        firework.setheading(angle)
        firework.pendown()
        firework.forward(distance)
        firework.penup()

# Main function to simulate multiple fireworks
def fireworks_show(num_fireworks):
    for _ in range(num_fireworks):
        # Random position for each firework burst
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        draw_firework(x, y)

# Set up color mode for RGB values
turtle.colormode(1.0)  # Use 0-1 range for RGB colors

# Run the fireworks show with 10 bursts
fireworks_show(10)

# Keep the window open
turtle.done()
