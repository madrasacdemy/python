import pygame
import random
import math

# Initialize pygame
pygame.init()
width, height = 1024, 768
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("🔥 Big Fire Animation")
clock = pygame.time.Clock()

# Particle lists
fire_particles = []
smoke_particles = []
MAX_FIRE = 700
MAX_SMOKE = 300

# Helper functions
def fire_color(life):
    return (
        255,
        min(255, int(160 + life * 0.7)),
        int(50 + life * 0.2)
    )

def smoke_color(alpha):
    return (120, 120, 120, alpha)

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fire particle generation
    for _ in range(10):
        if len(fire_particles) < MAX_FIRE:
            fire_particles.append({
                'x': random.randint(width//2 - 50, width//2 + 50),
                'y': height - 60,
                'vx': random.uniform(-1.2, 1.2),
                'vy': random.uniform(-6, -3),
                'life': random.randint(40, 100),
            })

    # Smoke particle generation
    for _ in range(2):
        if len(smoke_particles) < MAX_SMOKE:
            smoke_particles.append({
                'x': random.randint(width//2 - 30, width//2 + 30),
                'y': height - 80,
                'vx': random.uniform(-0.5, 0.5),
                'vy': random.uniform(-2, -1),
                'life': random.randint(80, 150),
            })

    # Draw fire particles
    for p in fire_particles[:]:
        p['x'] += p['vx']
        p['y'] += p['vy']
        p['vy'] *= 0.97
        p['life'] -= 1

        if p['life'] <= 0:
            fire_particles.remove(p)
            continue

        alpha = max(0, min(255, p['life'] * 3))
        color = fire_color(p['life'])
        surf = pygame.Surface((12, 12), pygame.SRCALPHA)
        pygame.draw.circle(surf, (*color, alpha), (6, 6), 6)
        screen.blit(surf, (int(p['x']) - 6, int(p['y']) - 6))

    # Draw smoke particles
    for s in smoke_particles[:]:
        s['x'] += s['vx']
        s['y'] += s['vy']
        s['vy'] *= 0.99
        s['life'] -= 1

        if s['life'] <= 0:
            smoke_particles.remove(s)
            continue

        alpha = max(0, min(180, s['life'] * 1.5))
        surf = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(surf, smoke_color(alpha), (10, 10), 10)
        screen.blit(surf, (int(s['x']) - 10, int(s['y']) - 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
