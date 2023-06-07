from math import cos, sin, pi, radians, dist
from constants import *
from drawboard import Board
import pygame
import sys


class Game:
    def __init__(self, screen):
        self.board = Board(SIZE)
        self.clock = pygame.time.Clock()
        self.playerTurn = True
        self.screen = screen
        self.boardMatrix = [[-1 for i in range(SIZE)] for j in range(SIZE)]

    def event_handler(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    print("Quit")

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = self.board.get_neareast_pos(*pygame.mouse.get_pos())
                    if pos is not None:
                        self.turn(*pos)
                    self.board.draw_board(self.boardMatrix, self.screen)
        pygame.quit()
        sys.exit()

    def turn(self, i, j):
        if self.boardMatrix[i][j] == -1:
            self.boardMatrix[i][j] = int(self.playerTurn)
            self.playerTurn = not self.playerTurn

    def play(self):
        print("Playing")
        self.board.draw_board(self.boardMatrix, self.screen)

        pygame.display.update()
        self.clock.tick(30)
        self.event_handler()
