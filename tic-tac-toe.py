#Tic-Tac-Toe Game
#pip install pygame
import pygame
import sys

pygame.init()

width = 300
height = 300
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic-Tac-Toe")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

grid_size = 3
cell_size = width // grid_size

board = [["" for _ in range(grid_size)] for _ in range(grid_size)]
current_player = "X"
game_over = False

font = pygame.font.SysFont("arial", 50)

def draw_board():
    window.fill(white)
    for i in range(1, grid_size):
        pygame.draw.line(window, black, (i * cell_size, 0), (i * cell_size, height), 3)
        pygame.draw.line(window, black, (0, i * cell_size), (width, i * cell_size), 3)

    for row in range(grid_size):
        for col in range(grid_size):
            if board[row][col] != "":
                text = font.render(board[row][col], True, black)
                window.blit(text, (col * cell_size + cell_size // 3, row * cell_size + cell_size // 6))
    
    pygame.display.update()

def check_winner():
    for i in range(grid_size):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]

    return None

def game_over_screen(winner):
    window.fill(white)
    if winner:
        text = font.render(f"{winner} Wins!", True, blue)
    else:
        text = font.render("It's a Draw!", True, red)
    window.blit(text, (width // 6, height // 3))
    pygame.display.update()

    pygame.time.delay(2000)  

running = True
while running:
    draw_board()

    winner = check_winner()
    if winner or all(board[row][col] != "" for row in range(grid_size) for col in range(grid_size)):
        game_over_screen(winner)
        board = [["" for _ in range(grid_size)] for _ in range(grid_size)]
        current_player = "X"
        game_over = False
        pygame.time.delay(1000) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            col = mouse_x // cell_size
            row = mouse_y // cell_size

            if board[row][col] == "":
                board[row][col] = current_player
                current_player = "O" if current_player == "X" else "X" 

    pygame.display.update()

pygame.quit()
sys.exit()
