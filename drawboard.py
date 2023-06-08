import pygame
from pygame.gfxdraw import filled_polygon, aapolygon
from math import cos, sin, pi, radians
from pygame import gfxdraw
from constants import *

class Board:
    def __init__(self, size):
        self.size = size
        self.gap = 1.04

    def hexagon(self, x, y, screen, color):
        corners = [(x + (HEX_RADIUS * self.gap) * cos(radians(90) + 2 * pi * _ / 6),
                    y + (HEX_RADIUS * self.gap) * sin(radians(90) + 2 * pi * _ / 6))
                    for _ in range(6)]

        filled_polygon(screen, corners, color)  # Inner fill
        aapolygon(screen, corners, BLACK)  # Outline


    def get_pixel_coords(self, i, j):
        x = HEX_OFFSET + (2 * HEX_RADIUS) * i + HEX_RADIUS * j  # MATH
        y = HEX_OFFSET + (1.75 * HEX_RADIUS) * j   # MATH

        return x, y

    def get_neareast_pos(self, x, y):
        j = round(4 * (y - HEX_OFFSET) / (7 * HEX_RADIUS))  # MATH
        i = round(- (3 * HEX_OFFSET - 7 * x + 4 * y) / (14 * HEX_RADIUS))  # MATH
        if i < 0 or i >= self.size or j < 0 or j >= self.size:
            return None
        return i, j

    def draw_boarder(self, screen):
        corners = []
        topRowCorners = []
        leftRowCorners = []
        rightRowCorners = []
        bottomRowCorners = []
        borderSize = 2.5
        cornerCoords = [self.get_pixel_coords(0, 0),
                        self.get_pixel_coords(self.size - 1, 0),
                        self.get_pixel_coords(0, self.size-1),
                        self.get_pixel_coords(self.size-1, self.size-1)]
        # find corner coordinates

        # top left TODO
        topRowCorners.append((cornerCoords[0][0] + (HEX_RADIUS * self.gap) * cos(radians(90) + 2 * pi * 2 / 6),
                        cornerCoords[0][1] + (HEX_RADIUS * self.gap) * sin(radians(90) + 2 * pi * 2 / 6)))
        # top right
        topRowCorners.append((cornerCoords[1][0] + (HEX_RADIUS * self.gap) * cos(radians(90) + 2 * pi * 3.39 / 6),
                        cornerCoords[1][1] + (HEX_RADIUS * self.gap) * sin(radians(90) + 2 * pi * 3.81 / 6)))
        """
        # bottom left
        corners.append((cornerCoords[2][0] + (12 * self.gap) * cos(radians(90) + 2 * pi * 0.55 / 6),
                        cornerCoords[2][1] + (HEX_RADIUS * self.gap) * sin(radians(90) + 2 * pi * 1 / 6)))
        # bottom right
        corners.append((cornerCoords[3][0] + (HEX_RADIUS * self.gap) * cos(radians(90) + 2 * pi * 5 / 6),
                        cornerCoords[3][1] + (HEX_RADIUS * self.gap) * sin(radians(90) + 2 * pi * 5 / 6)))

        #calculate border corners
        # top left
        corners.append((cornerCoords[0][0] + (HEX_RADIUS * borderSize) * cos(radians(90) + 2 * pi * 2 / 6),
                        cornerCoords[0][1] + (HEX_RADIUS * borderSize) * sin(radians(90) + 2 * pi * 2 / 6)))
        # top right
        corners.append((cornerCoords[1][0] + (12 * borderSize) * cos(radians(90) + 2 * pi * 3.55 / 6),
                        cornerCoords[1][1] + (HEX_RADIUS * borderSize) * sin(radians(90) + 2 * pi * 4 / 6)))
        # bottom left
        corners.append((cornerCoords[2][0] + (12 * borderSize) * cos(radians(90) + 2 * pi * 0.55 / 6),
                        cornerCoords[2][1] + (HEX_RADIUS * borderSize) * sin(radians(90) + 2 * pi * 1 / 6)))
        # bottom right
        corners.append((cornerCoords[3][0] + (HEX_RADIUS * borderSize) * cos(radians(90) + 2 * pi * 5 / 6),
                        cornerCoords[3][1] + (HEX_RADIUS * borderSize) * sin(radians(90) + 2 * pi * 5 / 6)))
        """
        """
        filled_polygon(screen, [corners[4],corners[0],corners[1],corners[5]], PLAYER_COLORS[0])
        filled_polygon(screen, [corners[5], corners[1], corners[3], corners[7]], PLAYER_COLORS[1])
        filled_polygon(screen, [corners[3], corners[7], corners[6], corners[2]], PLAYER_COLORS[0])
        filled_polygon(screen, [corners[2], corners[6], corners[4], corners[0]], PLAYER_COLORS[1])


        aapolygon(screen, [corners[4],corners[0],corners[1],corners[5]], BLACK)
        aapolygon(screen, [corners[5], corners[1], corners[3], corners[7]], BLACK)
        aapolygon(screen, [corners[3], corners[7], corners[6], corners[2]], BLACK)
        aapolygon(screen, [corners[2], corners[6], corners[4], corners[0]], BLACK)
        """

        """
        cornerHelper = [0, 1, 6]
        for i in range(self.size):
            for j in range(self.size):
                x, y = self.get_pixel_coords(i, j)
                if i == 0:  # left row
                    for n in range(0, 3):
                        leftRowCorners.append((x + (HEX_RADIUS * self.gap) * cos(radians(90) + 2 * pi * n / 6),
                                                y + (HEX_RADIUS * self.gap) * sin(radians(90) + 2 * pi * n / 6)))
                elif i == self.size - 1:  # right row
                    for n in range(3, 6):
                        rightRowCorners.append((x + (HEX_RADIUS * self.gap) * cos(radians(90) + 2 * pi * n / 6),
                                                y + (HEX_RADIUS * self.gap) * sin(radians(90) + 2 * pi * n / 6)))
                elif j == 0:  # top row
                    for n in range(2, 5):
                        topRowCorners.append((x + (HEX_RADIUS * self.gap) * cos(radians(90) + 2 * pi * n / 6),
                                                y + (HEX_RADIUS * self.gap) * sin(radians(90) + 2 * pi * n / 6)))
                elif j == self.size - 1:  # bottom row
                    for n in cornerHelper:
                        bottomRowCorners.append((x + (HEX_RADIUS * self.gap) * cos(radians(90) + 2 * pi * n / 6),
                                                y + (HEX_RADIUS * self.gap) * sin(radians(90) + 2 * pi * n / 6)))
        """

        #corners = [topRowCorners,leftRowCorners,rightRowCorners,bottomRowCorners]
        for point in topRowCorners:
            pygame.draw.circle(screen, RED, point, 2)

        pygame.display.update()

    def draw_board(self, matrix, screen):
        self.draw_boarder(screen)
        for i in range(self.size):
            for j in range(self.size):
                x, y = self.get_pixel_coords(i, j)
                self.hexagon(x, y, screen, PLAYER_COLORS[matrix[i][j]])
        self.draw_boarder(screen)
        pygame.display.update()




