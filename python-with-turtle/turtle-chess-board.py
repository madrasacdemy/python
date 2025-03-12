import turtle

# Draw the chessboard
def draw_board():
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.pensize(2)
    
    for row in range(8):
        for col in range(8):
            x = col * 50 - 200
            y = row * 50 - 200
            if (row + col) % 2 == 0:
                color = "white"
            else:
                color = "black"
            draw_square(x, y, 50, color)

def draw_square(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

def move_piece(piece, x, y):
    piece.goto(x, y)

# Draw the chessboard
draw_board()

# Create a movable piece (example: a red circle as a pawn)
pawn = turtle.Turtle()
pawn.shape("circle")
pawn.color("red")
pawn.penup()
pawn.goto(-175, -175)  # Starting position

# Move the piece interactively
def on_click(x, y):
    move_piece(pawn, x, y)

turtle.onscreenclick(on_click)
turtle.done()
