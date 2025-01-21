#Please install this "pip install pygame" before you run the program 
import pygame
import random

pygame.init()

# Screen dimensions
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Brick Breaker")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# Paddle
paddle_width = 100
paddle_height = 10
paddle_x = (width - paddle_width) // 2
paddle_y = height - 20
paddle_speed = 10

# Ball
ball_radius = 10
ball_x = width // 2
ball_y = height // 2
ball_dx = random.choice([-4, 4])
ball_dy = -4

# Bricks
brick_rows = 5
brick_cols = 10
brick_width = width // brick_cols
brick_height = 20
bricks = []
for row in range(brick_rows):
    for col in range(brick_cols):
        bricks.append(pygame.Rect(col * brick_width, row * brick_height, brick_width, brick_height))

# Score
score = 0
font = pygame.font.SysFont("comicsansms", 30)

def draw_bricks():
    for brick in bricks:
        pygame.draw.rect(window, green, brick)

def display_score():
    text = font.render(f"Score: {score}", True, white)
    window.blit(text, (10, 10))

# Game loop
running = True
while running:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < width - paddle_width:
        paddle_x += paddle_speed

    # Ball movement
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with walls
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= width:
        ball_dx *= -1
    if ball_y - ball_radius <= 0:
        ball_dy *= -1
    if ball_y + ball_radius >= height:
        running = False  # Game over

    # Ball collision with paddle
    paddle = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    if paddle.colliderect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2):
        ball_dy *= -1

    # Ball collision with bricks
    for brick in bricks[:]:
        if brick.colliderect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2):
            bricks.remove(brick)
            ball_dy *= -1
            score += 1

    # Draw everything
    window.fill(black)
    draw_bricks()
    pygame.draw.rect(window, blue, paddle)
    pygame.draw.circle(window, red, (ball_x, ball_y), ball_radius)
    display_score()
    pygame.display.update()

pygame.quit()
