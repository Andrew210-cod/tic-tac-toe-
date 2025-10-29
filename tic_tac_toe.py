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

pygame.display.update()
 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
    

