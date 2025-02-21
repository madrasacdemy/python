import turtle

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fractal Tree")

# Create the turtle
tree = turtle.Turtle()
tree.color("green")
tree.speed(0)  # Fastest drawing speed
tree.hideturtle()

# Recursive function to draw the fractal tree
def draw_branch(branch_length, angle):
    if branch_length > 5:  # Base case to stop recursion
        # Draw the main branch
        tree.forward(branch_length)

        # Draw the right branch
        tree.right(angle)
        draw_branch(branch_length - 15, angle)

        # Return to the original position
        tree.left(2 * angle)
        draw_branch(branch_length - 15, angle)

        # Return to the original angle
        tree.right(angle)
        tree.backward(branch_length)

# Main function
def draw_fractal_tree():
    tree.penup()
    tree.goto(0, -250)  # Start from the bottom of the screen
    tree.left(90)  # Point turtle upwards
    tree.pendown()

    # Start the recursive drawing
    draw_branch(100, 30)

# Run the program
draw_fractal_tree()

# Keep the window open
turtle.done()
