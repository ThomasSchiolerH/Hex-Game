from math import cos, sin, pi, radians, dist

from pygame import gfxdraw

from drawboard import Board
import pygame
import sys
import numpy as np
from scipy.spatial.distance import cdist


class Game:
    def __init__(self, boardSize: int = 6):
        self.board = Board()
        self.playerTurnColor = [(255, 0, 0), (0, 0, 255)]
        self.playerTurn = 0
        rows = cols = self.board.boardSize
        self.boardMatrix = [[-1 for i in range(cols)] for j in range(rows)]

    def event_handler(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    print("Quit")

                if event.type == pygame.MOUSEBUTTONDOWN:
                    passableTurn = self.turn()
                    if passableTurn:
                        if self.playerTurn == 0:
                            self.playerTurn = 1
                        elif self.playerTurn == 1:
                            self.playerTurn = 0

        pygame.quit()
        sys.exit()

    def turn(self):
        correct = False
        selectedTile = self.getNearestTile()
        x, y = self.board.hexDictionary[selectedTile][6]
        if self.board.tileColored(x, y):
            self.board.drawChosenTile(x, y, self.playerTurnColor[self.playerTurn])
            self.makeMoveInMatrix(selectedTile)
            correct = True
        return correct

    def makeMoveInMatrix(self, tile):
        row = tile // self.board.boardSize
        column = tile % self.board.boardSize

        self.boardMatrix[row][column] = self.playerTurn

    def getNearestTile(self):
        nearestTile = None
        minDist = 6000

        for i in self.board.hexDictionary:
            distance = dist(pygame.mouse.get_pos(), self.board.hexDictionary[i][6])
            if distance < minDist:
                minDist = distance
                nearestTile = i
        return nearestTile

    def play(self):
        print("Playing")
        self.board.draw_board()

        pygame.display.update()
        self.board.clock.tick(30)
        self.event_handler()
