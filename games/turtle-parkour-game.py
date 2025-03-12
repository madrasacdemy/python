import turtle
import random

# Screen setup
turtle.setup(600, 400)
turtle.bgcolor("lightblue")
turtle.title("Turtle Parkour Game")
turtle.tracer(0)

# Player setup
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.goto(-250, -150)
player.dy = 0  # Jump velocity

ground_level = -150

def draw_ground():
    ground = turtle.Turtle()
    ground.hideturtle()
    ground.penup()
    ground.goto(-300, ground_level - 10)
    ground.pendown()
    ground.color("brown")
    ground.begin_fill()
    for _ in range(2):
        ground.forward(600)
        ground.right(90)
        ground.forward(20)
        ground.right(90)
    ground.end_fill()

draw_ground()

# Obstacles
obstacles = []

def create_obstacle():
    obstacle = turtle.Turtle()
    obstacle.shape("square")
    obstacle.color("red")
    obstacle.penup()
    obstacle.goto(300, ground_level + 10)
    obstacles.append(obstacle)

def move_obstacles():
    for obstacle in obstacles[:]:
        obstacle.setx(obstacle.xcor() - 5)
        if obstacle.xcor() < -300:
            obstacles.remove(obstacle)
            obstacle.hideturtle()
    if random.random() < 0.02:  # Random obstacle generation
        create_obstacle()

def jump():
    if player.ycor() == ground_level:
        player.dy = 10

def update_game():
    global player
    player.sety(player.ycor() + player.dy)
    player.dy -= 0.5  # Gravity effect
    if player.ycor() < ground_level:
        player.sety(ground_level)
        player.dy = 0
    
    move_obstacles()
    for obstacle in obstacles:
        if player.distance(obstacle) < 20:
            print("Game Over!")
            return
    
    turtle.update()
    turtle.ontimer(update_game, 50)

# Key bindings
turtle.listen()
turtle.onkey(jump, "space")

# Start game
update_game()
turtle.done()