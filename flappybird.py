#Please install this "pip install pygame" before you run the program 
import pygame
import random

pygame.init()

width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

bird_x = 100
bird_y = height // 2
bird_radius = 15
bird_velocity = 0
gravity = 0.5
jump_strength = -8

pipe_width = 80
pipe_gap = 150
pipe_speed = 5
pipes = []
pipe_frequency = 1500 
last_pipe_time = pygame.time.get_ticks()

score = 0
font = pygame.font.SysFont("arial", 35)

def display_score():
    text = font.render(f"Score: {score}", True, black)
    window.blit(text, (10, 10))

def game_over_screen():
    window.fill(blue)
    text = font.render("Game Over! Press R to Restart or Q to Quit", True, white)
    window.blit(text, (width // 10, height // 2))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: 
                    return True
                if event.key == pygame.K_q: 
                    pygame.quit()
                    quit()

running = True
while running:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = jump_strength

    bird_velocity += gravity
    bird_y += bird_velocity

    current_time = pygame.time.get_ticks()
    if current_time - last_pipe_time > pipe_frequency:
        pipe_height = random.randint(100, height - pipe_gap - 100)
        pipes.append((width, pipe_height))
        last_pipe_time = current_time

    pipes = [(x - pipe_speed, h) for x, h in pipes if x > -pipe_width]
    for x, h in pipes:
        if bird_x + bird_radius > x and bird_x - bird_radius < x + pipe_width:
            if bird_y - bird_radius < h or bird_y + bird_radius > h + pipe_gap:
                if game_over_screen(): 
                    bird_y = height // 2
                    bird_velocity = 0
                    pipes = []
                    score = 0
                    break
                else:
                    running = False

    if bird_y - bird_radius <= 0 or bird_y + bird_radius >= height:
        if game_over_screen():  
            bird_y = height // 2
            bird_velocity = 0
            pipes = []
            score = 0
        else:
            running = False

    for x, h in pipes:
        if x + pipe_width // 2 == bird_x:
            score += 1

    window.fill(blue)
    pygame.draw.circle(window, red, (bird_x, bird_y), bird_radius)
    for x, h in pipes:
        pygame.draw.rect(window, green, (x, 0, pipe_width, h))
        pygame.draw.rect(window, green, (x, h + pipe_gap, pipe_width, height - h - pipe_gap))
    display_score()
    pygame.display.update()

pygame.quit()
