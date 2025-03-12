import turtle
import random
import time
import heapq

# Screen setup
turtle.setup(600, 600)
turtle.bgcolor("white")
turtle.title("Turtle AI Maze Solver")

# Maze configuration
grid_size = 20
maze = [[1 if random.random() < 0.2 else 0 for _ in range(grid_size)] for _ in range(grid_size)]
maze[0][0] = 0  # Start point
maze[grid_size - 1][grid_size - 1] = 0  # End point

# Draw the maze
def draw_maze():
    turtle.speed(0)
    turtle.penup()
    for y in range(grid_size):
        for x in range(grid_size):
            if maze[y][x] == 1:
                turtle.goto(x * 20 - 200, 200 - y * 20)
                turtle.pendown()
                turtle.begin_fill()
                for _ in range(4):
                    turtle.forward(20)
                    turtle.right(90)
                turtle.end_fill()
                turtle.penup()

turtle.color("black")
draw_maze()

# AI Solver using A* Algorithm
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    cost_so_far = {start: 0}
    
    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            break
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_pos = (current[0] + dx, current[1] + dy)
            if 0 <= next_pos[0] < grid_size and 0 <= next_pos[1] < grid_size and maze[next_pos[1]][next_pos[0]] == 0:
                new_cost = cost_so_far[current] + 1
                if next_pos not in cost_so_far or new_cost < cost_so_far[next_pos]:
                    cost_so_far[next_pos] = new_cost
                    priority = new_cost + heuristic(goal, next_pos)
                    heapq.heappush(open_list, (priority, next_pos))
                    came_from[next_pos] = current
    
    return came_from

def draw_path(path):
    turtle.color("blue")
    turtle.penup()
    turtle.goto(-200 + path[0][0] * 20 + 10, 200 - path[0][1] * 20 - 10)
    turtle.pendown()
    for pos in path:
        turtle.goto(-200 + pos[0] * 20 + 10, 200 - pos[1] * 20 - 10)
        time.sleep(0.1)

# Solve the maze
start = (0, 0)
goal = (grid_size - 1, grid_size - 1)
came_from = a_star_search(start, goal)

# Reconstruct path
path = []
current = goal
while current != start:
    path.append(current)
    current = came_from.get(current, start)
path.append(start)
path.reverse()

draw_path(path)
turtle.done()
