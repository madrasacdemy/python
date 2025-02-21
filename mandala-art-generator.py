import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Mandala Art Generator")

# Create the turtle
artist = turtle.Turtle()
artist.speed(0)  # Fastest speed
artist.hideturtle()

# Function to draw a symmetrical mandala pattern
def draw_mandala(radius, num_petals):
    angle = 360 / num_petals
    for _ in range(num_petals):
        artist.circle(radius)
        artist.left(angle)

# Function to generate a mandala with random colors and layers
def generate_mandala(layers):
    for _ in range(layers):
        # Random radius, petal count, and color
        radius = random.randint(20, 100)
        num_petals = random.randint(6, 20)
        color = (random.random(), random.random(), random.random())  # Random RGB color
        artist.color(color)
        draw_mandala(radius, num_petals)
        artist.left(20)  # Slight rotation to create layered effect

# Main function
def main():
    # Set up turtle for RGB color mode
    turtle.colormode(1.0)  # Use 0-1 range for RGB
    # Generate 5 layers of random mandala patterns
    generate_mandala(5)
    # Keep the window open
    turtle.done()

# Run the program
main()
