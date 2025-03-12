import turtle
import random
import time

# Setup screen
turtle.setup(600, 600)
turtle.bgcolor("black")
turtle.title("Turtle Space Invaders")

turtle.tracer(0, 0)

turtle.hideturtle()

# Player setup
player = turtle.Turtle()
player.shape("triangle")
player.color("white")
player.penup()
player.goto(0, -250)
player.setheading(90)

# Bullet setup
bullet = turtle.Turtle()
bullet.shape("square")
bullet.color("red")
bullet.shapesize(0.2, 1)
bullet.penup()
bullet.hideturtle()

# Enemy setup
enemies = []
num_enemies = 6

def create_enemy():
    enemy = turtle.Turtle()
    enemy.shape("circle")
    enemy.color(random.choice(["green", "blue", "purple", "yellow"]))
    enemy.penup()
    enemy.goto(random.randint(-250, 250), random.randint(100, 250))
    enemies.append(enemy)

for _ in range(num_enemies):
    create_enemy()

# Score setup
score = 0
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-280, 260)

def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}", font=("Arial", 16, "bold"))

update_score()

# Player movement
def move_left():
    x = player.xcor()
    if x > -280:
        player.setx(x - 20)

def move_right():
    x = player.xcor()
    if x < 280:
        player.setx(x + 20)

def fire_bullet():
    if not bullet.isvisible():
        bullet.goto(player.xcor(), player.ycor() + 10)
        bullet.showturtle()

def update_game():
    global score, enemies
    if bullet.isvisible():
        bullet.sety(bullet.ycor() + 20)
        if bullet.ycor() > 280:
            bullet.hideturtle()
    
    for enemy in enemies[:]:
        enemy.sety(enemy.ycor() - 2)
        if enemy.distance(bullet) < 20 and bullet.isvisible():
            enemy.hideturtle()
            enemies.remove(enemy)
            bullet.hideturtle()
            score += 10
            update_score()
            create_enemy()
        if enemy.ycor() < -250:
            enemy.goto(random.randint(-250, 250), random.randint(100, 250))
    
    turtle.update()
    turtle.ontimer(update_game, 50)

# Key bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Start game
update_game()
turtle.done()