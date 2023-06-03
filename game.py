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


    def event_handler(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    print("Quit")
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.turn()
        
        pygame.quit()
        sys.exit()

    def turn(self):
        print(self.getNearestTile())

        gfxdraw.filled_polygon(self.board.screen,
                                [(50 + self.board.hex_radius * cos(radians(90) + 2 * pi * _ / 6),
                                50 + self.board.hex_radius * sin(radians(90) + 2 * pi * _ / 6))
                                for _ in range(6)],
                               (255,0,0))


    def getNearestTile(self):
        nearestTile = None
        minDist = 6000

        for i in self.board.hexDictionary:
            distance = dist(pygame.mouse.get_pos(), self.board.hexDictionary[i][0])
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


