import pygame
import pygame.gfxdraw
from math import cos, sin, pi, radians
from pygame import gfxdraw

class drawboard:
    def __init__(self):
        pygame.init()
        clock = pygame.time.Clock()

        self.black = (40, 40, 40)
        self.boardSize = 6
        self.hex_radius = 20
        self.x_offset, self.y_offset = 60, 60
        self.text_offset = 45
        self.hexDictionary = {}

        #window size and color
        self.screen = pygame.display.set_mode((800, 600))
        self.screen.fill((255, 255, 255))

        #object
        self.s = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA, 32)

        for i in range(3):
            pygame.draw.line(self.s, (255, 0, 0), (400, 300 + i * 100), (400 + 200, 300+ i * 100), 4)

        self.screen.blit(self.s, (0, 0))

        #run with 30 fps
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()
            clock.tick(30)

        pygame.quit()
        quit()


    def drawHexagon(self, surface, color: tuple, position: tuple, node: int):
        polyEdges = 6
        x, y = position
        offset = 3

        self.hexDictionary[node] = [(x + (self.hex_radius + offset) * cos(radians(90) + 2 * pi * _ / polyEdges),
                                  y + (self.hex_radius + offset) * sin(radians(90) + 2 * pi * _ / polyEdges))
                                 for _ in range(polyEdges)]

        gfxdraw.aapolygon(self.s, self.hexDictionary[node], color)

    def draw_board(self):
        counter = 0
        for row in range(self.boardSize):
            for column in range(self.boardSize):
                self.drawHexagon(self.screen, self.black, self.get_coordinates(row, column), counter)
                counter += 1

    def get_coordinates(self, row: int, column: int):
        x = self.x_offset + (2 * self.hex_radius) * column + self.hex_radius * row
        y = self.y_offset + (1.75 * self.hex_radius) * row

        return x, y





