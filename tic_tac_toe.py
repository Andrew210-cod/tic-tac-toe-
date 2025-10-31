import pygame 
from pygame.locals import *

pygame.init()
pygame.font.init()

font = pygame.font.SysFont("Courier New", 40)

running = True 

window_size = (450, 500)


screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Tic Tac Toe")
screen.fill("brown")

class TicTacToe():
    def __init__(self, table_size):
        self.table_size = table_size
        self.cell_size = table_size // 3
        self.table_space = 20

        self.player = "X"
        self.winner = None
        self.taking_move = True
        self.running = True
        self.table = []
        for col in range(3):
            self.table.append([])
            for row in range(3):
                self.table[col].append("-")

        self.bckround_color = (255, 174, 66)
        self.table_color = (50, 50, 50)
        self.line_color = (190, 0, 10)
        self.intructions_color = (17, 53, 165)
        self.game_over_bg_color = (47, 98, 162)
        self.game_over_color = (255, 179, 1)
        self.font= pygame.font.SysFont("Courier New", 35)
        self.FPS = pygame.time.Clock()

# draw table representation 

def _draw_table(self):
    tb_space_point = (self.table_space, self.table_size - self.table_space)
    cell_space_point = (self.cell_size, self.ell_size * 2)
    r1 = pygame.draw.line (screen, self.table_color, [tb_space_point[0], cell_space_point[0]], [tb_space_point[1], cell_space_point[0]], 8)
    c1 = pygame.draw.line(screen, self.table_color, [cell_space_point[0], tb_space_point[0]], [cell_space_point[0], tb_space_point[1]], 8)
    r2 = pygame.draw.line (screen, self.table_color, [tb_space_point[0], cell_space_point[1]], [tb_space_point[1], cell_space_point[1]], 8)
    c2 = pygame.draw.line(screen, self.table_color, [cell_space_point[1], tb_space_point[0]], [tb_space_point[1], tb_space_point[1]], 8 )

def _chang_player(self):
    self.player = "O" if self.player == "X" else "X"

# processing clicks to move
def _move(self, pos):
    try:

        x, y = pos[0] // self.cell_size, pos[1] // self.cell_size
        if self.table[x][y] == "-":
            self.table[x][y] = self.player
            self._draw_char(x, y, self.player)
            self._game_check()
            self._chang_player()

    except:
        print("Click inside the table only")

#draw character of the reent player to the selected table cell
def _draw_char(self, x, y, player):
    if self.player == "O":
        img = pygame.image.load("images/Tc-O.png")

 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
    

