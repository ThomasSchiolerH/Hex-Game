import pygame
from pygame.gfxdraw import filled_polygon, aapolygon
from math import cos, sin, pi, radians
from pygame import gfxdraw
from constants import *

class Board:
    def __init__(self, size):
        self.size = size

    def hexagon(self, x, y, screen, color):
        resizer = 1.1
        corner = [(x + (HEX_RADIUS * resizer) * cos(radians(90) + 2 * pi * _ / 6),
                    y + (HEX_RADIUS * resizer) * sin(radians(90) + 2 * pi * _ / 6))
                    for _ in range(6)]

        filled_polygon(screen, corner, color)  # Inner fill
        aapolygon(screen, corner, BLACK)  # Outline


    def get_pixel_coords(self, i, j):
        x = HEX_OFFSET + (2 * HEX_RADIUS) * i + HEX_RADIUS * j  # MATH
        y = HEX_OFFSET + (1.75 * HEX_RADIUS) * j   # MATH

        return x, y

    def get_nearest_pos(self, x, y):
        j = round(4 * (y - HEX_OFFSET) / (7 * HEX_RADIUS))  # MATH
        i = round(- (3 * HEX_OFFSET - 7 * x + 4 * y) / (14 * HEX_RADIUS))  # MATH
        if i < 0 or i >= self.size or j < 0 or j >= self.size:
            return None
        return i, j

    def draw_board(self, matrix, screen, winner=None):
        for i in range(self.size):
            for j in range(self.size):
                x, y = self.get_pixel_coords(i, j)
                self.hexagon(x, y, screen, PLAYER_COLORS[matrix[i][j]])
        self.draw_winner_message(screen, winner)
        pygame.display.update()

    def draw_winner_message(self, screen, winner):
        if winner:
            font = pygame.font.Font(None, 36)
            text_surface = font.render(winner, True, BLACK)
            text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT - 50))
            screen.blit(text_surface, text_rect)
    def get_clicked_tile(self, mouse_pos):
        x, y = mouse_pos
        for i in range(self.size):
            for j in range(self.size):
                px, py = self.get_pixel_coords(i, j)
                dist = ((x - px) ** 2 + (y - py) ** 2) ** 0.5
                if dist <= HEX_RADIUS:
                    return i, j
        return None, None


