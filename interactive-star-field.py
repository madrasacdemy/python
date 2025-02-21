import turtle
import random
import time

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Interactive Star Field")

# Create the turtle for drawing stars
star_turtle = turtle.Turtle()
star_turtle.hideturtle()
star_turtle.speed(0)  # Fastest drawing speed

# Function to draw a star at a given position with a random size
def draw_star(x, y, size, color):
    star_turtle.penup()
    star_turtle.goto(x, y)
    star_turtle.pendown()
    star_turtle.color(color)

    star_turtle.begin_fill()
    for _ in range(5):
        star_turtle.forward(size)
        star_turtle.right(144)  # 144° angle to form a star shape
    star_turtle.end_fill()

# Function to generate random stars across the screen
def generate_stars(num_stars):
    stars = []
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        size = random.randint(5, 15)
        color = random.choice(["white", "lightyellow", "lightblue", "lightgray"])
        stars.append((x, y, size, color))
    return stars

# Function to twinkle and move stars
def animate_stars(stars):
    while True:
        star_turtle.clear()  # Clear the previous frame
        for i in range(len(stars)):
            x, y, size, color = stars[i]
            draw_star(x, y, size, color)

            # Twinkle effect: randomly change the size and color of stars
            if random.random() < 0.1:
                size = random.randint(5, 15)
                color = random.choice(["white", "lightyellow", "lightblue", "lightgray"])

            # Move the star slightly to simulate movement across the screen
            x += random.randint(-2, 2)
            y += random.randint(-1, 1)

            # Wrap the star around the screen if it moves out of bounds
            if x > 300:
                x = -300
            elif x < -300:
                x = 300
            if y > 300:
                y = -300
            elif y < -300:
                y = 300

            # Update the star's new position and attributes
            stars[i] = (x, y, size, color)

        time.sleep(0.05)  # Add a short delay for smooth animation

# Main function
def main():
    num_stars = 50  # Number of stars in the star field
    stars = generate_stars(num_stars)
    animate_stars(stars)

# Run the star field animation
main()

# Keep the window open
turtle.done()
