import pygame, sys, random

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Balls")

balls = [{
    'x': random.randint(50, width-50),
    'y': random.randint(50, height-50),
    'dx': random.uniform(-5, 5),
    'dy': random.uniform(-5, 5),
    'color': (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)),
    'radius': random.randint(10, 30)
} for _ in range(15)]

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    for ball in balls:
        ball['x'] += ball['dx']
        ball['y'] += ball['dy']

        if ball['x'] <= ball['radius'] or ball['x'] >= width - ball['radius']:
            ball['dx'] *= -1
        if ball['y'] <= ball['radius'] or ball['y'] >= height - ball['radius']:
            ball['dy'] *= -1

        pygame.draw.circle(screen, ball['color'], (int(ball['x']), int(ball['y'])), ball['radius'])

    pygame.display.flip()
    clock.tick(60)