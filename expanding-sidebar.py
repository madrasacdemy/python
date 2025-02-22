import turtle
import time

# Set up screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(600, 500)
screen.tracer(0)

# Sidebar settings
sidebar = turtle.Turtle()
sidebar.speed(0)
sidebar.color("cyan")
sidebar.penup()
sidebar.goto(-300, 250)
sidebar.pendown()

# Sidebar state
sidebar_width = 50
expanded_width = 200
collapsed_width = 50
expanded = False

# Buttons inside the menu
buttons = []

def draw_sidebar(width):
    """Draw the sidebar with a given width"""
    sidebar.clear()
    sidebar.penup()
    sidebar.goto(-300, 250)
    sidebar.pendown()
    sidebar.begin_fill()
    for _ in range(2):
        sidebar.forward(width)
        sidebar.right(90)
        sidebar.forward(500)
        sidebar.right(90)
    sidebar.end_fill()

def create_button(y_pos, label):
    """Create buttons inside the menu"""
    button = turtle.Turtle()
    button.speed(0)
    button.color("white")
    button.penup()
    button.goto(-280, y_pos)
    button.write(label, font=("Arial", 14, "bold"))
    buttons.append(button)

def toggle_sidebar(x, y):
    """Expand or collapse the sidebar when clicked"""
    global expanded
    if expanded:
        for w in range(expanded_width, collapsed_width, -10):  # Collapse animation
            draw_sidebar(w)
            screen.update()
            time.sleep(0.02)
        clear_buttons()
    else:
        for w in range(collapsed_width, expanded_width, 10):  # Expand animation
            draw_sidebar(w)
            screen.update()
            time.sleep(0.02)
        create_button(150, "Home")
        create_button(100, "Settings")
        create_button(50, "Exit")
    
    expanded = not expanded  # Toggle state

def clear_buttons():
    """Clear buttons when collapsing the sidebar"""
    for btn in buttons:
        btn.clear()
    buttons.clear()

# Draw initial sidebar
draw_sidebar(sidebar_width)

# Click event to toggle menu
screen.onclick(toggle_sidebar)

# Keep window open
turtle.done()
