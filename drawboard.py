import pygame
from pygame.gfxdraw import filled_polygon, aapolygon
from math import cos, sin, pi, radians
from pygame import gfxdraw
from constants import *

"""
    File By
    Author : @Marcus / SovereignPihl
    Author : @Jakob / Jakob-kild
    Author : @Thomas / ThomasSchiolerH

"""




class Board:
    def __init__(self, size):
        self.size = size
        self.gap = 1.04

    #    @Authors: Marcus
    def hexagon(self, x, y, screen, color):
        corners = [(x + (HEX_RADIUS * self.gap) * cos(radians(90) + 2 * pi * _ / 6),
                    y + (HEX_RADIUS * self.gap) * sin(radians(90) + 2 * pi * _ / 6))
                    for _ in range(6)]

        filled_polygon(screen, corners, color)  # Inner fill
        aapolygon(screen, corners, BLACK)  # Outline


    #    @Authors: Marcus
    def get_pixel_coords(self, i, j):
        x = HEX_OFFSET + (2 * HEX_RADIUS) * i + HEX_RADIUS * j  # MATH
        y = HEX_OFFSET + (1.75 * HEX_RADIUS) * j   # MATH

        return x, y

    #    @Authors: Marcus
    def get_nearest_pos(self, x, y):
        j = round(4 * (y - HEX_OFFSET) / (7 * HEX_RADIUS))  # MATH
        i = round(- (3 * HEX_OFFSET - 7 * x + 4 * y) / (14 * HEX_RADIUS))  # MATH
        if i < 0 or i >= self.size or j < 0 or j >= self.size:
            return None
        return i, j

    #    @Authors: Jakob
    def draw_border(self, screen):
        topRowCorners = []
        leftRowCorners = []
        rightRowCorners = []
        bottomRowCorners = []
        borderSize = 2.7
        cornerCoords = [self.get_pixel_coords(0, 0),
                        self.get_pixel_coords(self.size - 1, 0),
                        self.get_pixel_coords(0, self.size-1),
                        self.get_pixel_coords(self.size-1, self.size-1)]

        # construct border points for top row
        topRowCorners.append((cornerCoords[0][0] + (HEX_RADIUS * borderSize) * cos(radians(90) + 2 * pi * 2 / 6),
                              cornerCoords[0][1] + (HEX_RADIUS * borderSize) * sin(radians(90) + 2 * pi * 2 / 6)))
        topRowCorners.extend(self.findPolygonPoints("topRowCorners"))
        topRowCorners.pop(len(topRowCorners) - 1)
        topRowCorners.append((cornerCoords[1][0] + (24 * self.gap) * cos(radians(90) + 2 * pi * 3.39 / 6),
                              cornerCoords[1][1] + (21 * self.gap) * sin(radians(90) + 2 * pi * 3.81 / 6)))

        topRowCorners.append((cornerCoords[1][0] + (12 * borderSize) * cos(radians(90) + 2 * pi * 3.55 / 6),
                              cornerCoords[1][1] + (HEX_RADIUS * borderSize) * sin(radians(90) + 2 * pi * 4 / 6)))

        # construct border points for right row
        rightRowCorners.append(topRowCorners[len(topRowCorners) - 1])
        rightRowCorners.append(topRowCorners[len(topRowCorners) - 2])
        rightRowCorners.extend(self.findPolygonPoints("rightRowCorners"))
        rightRowCorners.pop(2)
        rightRowCorners.append((cornerCoords[3][0] + (HEX_RADIUS * borderSize) * cos(radians(90) + 2 * pi * 5 / 6),
                        cornerCoords[3][1] + (HEX_RADIUS * borderSize) * sin(radians(90) + 2 * pi * 5 / 6)))

        # construct border points for bottom row
        bottomRowCorners.append((cornerCoords[2][0] + (12 * borderSize) * cos(radians(90) + 2 * pi * 0.55 / 6),
                                 cornerCoords[2][1] + (HEX_RADIUS * borderSize) * sin(radians(90) + 2 * pi * 1 / 6)))
        bottomRowCorners.append((cornerCoords[2][0] + (24 * self.gap) * cos(radians(90) + 2 * pi * 0.39 / 6),
                                cornerCoords[2][1] + (21 * self.gap) * sin(radians(90) + 2 * pi * 0.81 / 6)))
        bottomRowCorners.extend(self.findPolygonPoints("bottomRowCorners"))
        bottomRowCorners.pop(2)
        bottomRowCorners.extend(rightRowCorners[-2:])

        # construct border points for left
        leftRowCorners.append(topRowCorners[0])
        leftRowCorners.extend(self.findPolygonPoints("leftRowCorners"))
        leftRowCorners.pop(len(leftRowCorners) - 1)
        leftRowCorners.extend([bottomRowCorners[1], bottomRowCorners[0]])

        borders = [topRowCorners, rightRowCorners, bottomRowCorners, leftRowCorners]
        self.drawPolygonBorders(screen, borders)

    #    @Authors: Jakob
    def drawPolygonBorders(self, screen, borderList):
        color = 0
        for border in borderList:
            filled_polygon(screen, border, PLAYER_COLORS[color])
            aapolygon(screen, border, BLACK)
            if color == 0:
                color = 1
            else:
                color = 0

    #    @Authors: Jakob
    def findPolygonPoints(self, cornerArray):
        points = []
        if cornerArray == "topRowCorners":
            for i in range(self.size):
                x, y = self.get_pixel_coords(i, 0)
                points.extend(self.hexagonPoints(x, y, [2, 3, 4]))
        elif cornerArray == "rightRowCorners":
            for i in range(self.size):
                x, y = self.get_pixel_coords(self.size-1, i)
                points.extend(self.hexagonPoints(x, y, [3, 4, 5]))
        elif cornerArray == "bottomRowCorners":
            for i in range(self.size):
                x, y = self.get_pixel_coords(i, self.size-1)
                points.extend(self.hexagonPoints(x, y, [1, 0, 5]))
        elif cornerArray == "leftRowCorners":
            for i in range(self.size):
                x, y = self.get_pixel_coords(0, i)
                points.extend(self.hexagonPoints(x, y, [2, 1, 0]))
        return points

    #    @Authors: Jakob
    def hexagonPoints(self, x, y, edges):
        points = []
        for i in edges:
            points.append((x + (HEX_RADIUS * self.gap) * cos(radians(90) + 2 * pi * i / 6),
                           y + (HEX_RADIUS * self.gap) * sin(radians(90) + 2 * pi * i / 6)))
        return points

    #    @Authors: Jakob
    def colorWinPath(self, path, screen, playerColor):
        for point in path:
            x, y = self.get_pixel_coords(point[0], point[1])
            self.hexagon(x, y, screen, playerColor)
        pygame.display.update()


    #    @Authors: Marcus
    def draw_board(self, matrix, screen):
        screen.fill(BACKGROUND_COLOUR)
        self.draw_border(screen)
        for i in range(self.size):
            for j in range(self.size):
                x, y = self.get_pixel_coords(i, j)
                self.hexagon(x, y, screen, PLAYER_COLORS[matrix[i][j]])
        pygame.display.update()



    #    @Authors: Marcus
    def display_message(self, message, x_disp, y_disp, color, screen):
        font = pygame.font.Font('freesansbold.ttf', 28)
        text_surf = font.render(message, True, color)
        text_rect = text_surf.get_rect()
        text_rect = x_disp, y_disp
        screen.blit(text_surf, text_rect)
        pygame.display.update()

    #    @Authors: Jakob
    def getGameResolution(self, size):
        width = 2 * HEX_OFFSET + (1.75 * HEX_RADIUS) * size + HEX_RADIUS * size
        height = 2 * HEX_OFFSET + (1.75 * HEX_RADIUS) * size

        return (width, height)

    #    @Authors: Thomas
    def display_winner_box(self, winner, screen):
        # Create a font and render the winner text
        font = pygame.font.Font(None, 48)
        if not winner:
            text = font.render(f"Blue Player wins!", True, (255, 255, 255))
        else:
            text = font.render(f"Red Player wins!", True, (255, 255, 255))

        # Calculate the dimensions and position of the box
        box_width = text.get_width() + 20
        box_height = text.get_height() + 20
        width, height = self.getGameResolution(self.size)
        box_x = (width - box_width) // 2
        box_y = (height - box_height) // 2

        # Create a transparent surface for the box
        box_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
        border_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
        text_surface = pygame.Surface(text.get_size(), pygame.SRCALPHA)

        # Set the desired transparency -> 128 = 50%
        alpha_value = 128

        # Fill the surfaces with the desired transparency
        box_surface.fill((0, 0, 0, alpha_value))
        border_surface.fill((255, 255, 255, alpha_value))
        text_surface.fill((255, 255, 255, alpha_value))

        # Draw the border onto the box surface
        pygame.draw.rect(box_surface, (255, 255, 255, alpha_value), (0, 0, box_width, box_height), 2)

        # Blit the box, border, and text onto the screen
        screen.blit(box_surface, (box_x, box_y))
        screen.blit(border_surface, (box_x, box_y))
        screen.blit(text, (box_x + 10, box_y + 10))

        pygame.display.flip()


