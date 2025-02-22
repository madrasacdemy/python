import turtle
import math
import time

# Screen setup
turtle.bgcolor("black")
turtle.tracer(0)

# Create Sun
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.color("yellow")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

# Planet details (name, distance from sun, size, color, speed)
planets = [
    {"name": "Mercury", "distance": 70, "size": 5, "color": "gray", "speed": 0.2},
    {"name": "Venus", "distance": 100, "size": 8, "color": "orange", "speed": 0.15},
    {"name": "Earth", "distance": 140, "size": 10, "color": "blue", "speed": 0.1},
    {"name": "Mars", "distance": 180, "size": 7, "color": "red", "speed": 0.08},
    {"name": "Jupiter", "distance": 220, "size": 15, "color": "brown", "speed": 0.05},
    {"name": "Saturn", "distance": 260, "size": 13, "color": "gold", "speed": 0.04},
    {"name": "Uranus", "distance": 300, "size": 12, "color": "lightblue", "speed": 0.03},
    {"name": "Neptune", "distance": 340, "size": 11, "color": "blue", "speed": 0.025}
]

# Create turtle objects for planets
planet_turtles = []
orbits = []
for planet in planets:
    t = turtle.Turtle()
    t.shape("circle")
    t.color(planet["color"])
    t.shapesize(planet["size"] / 10)
    t.penup()
    planet_turtles.append(t)
    
    # Draw orbit circles
    orbit = turtle.Turtle()
    orbit.speed(0)
    orbit.color("white")
    orbit.penup()
    orbit.goto(0, -planet["distance"])
    orbit.pendown()
    orbit.circle(planet["distance"])
    orbit.hideturtle()
    orbits.append(orbit)

# Animate planets
angle = 0
while True:
    turtle.update()
    time.sleep(0.02)
    angle += 1
    for i, planet in enumerate(planets):
        x = planet["distance"] * math.cos(math.radians(angle * planet["speed"]))
        y = planet["distance"] * math.sin(math.radians(angle * planet["speed"]))
        planet_turtles[i].goto(x, y)