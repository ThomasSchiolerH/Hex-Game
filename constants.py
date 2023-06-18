import pygame
import pygame_menu
import pygame_menu.font as pmfont



"""
    File By
    Author : All

"""



# Multiplayer
PORT = 9009

WINDOW_NAME = "HEX BOARD GAME"

# Colours
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
LIGHT_GREY = (170, 170, 170)
DARK_GREY = (100, 100, 100)
WINCOLORS = [(145, 236, 250),(252, 111, 111)]
BACKGROUND_COLOUR = (40, 41, 35)

# Board
HEX_RADIUS = 20
TEXT_OFFSET = 45
HEX_OFFSET = 95

# Restart button dimensions and position
restartPos = pygame.Rect(10, 10, 100, 40)

# Multiplayer
SERVER_IP = "25.66.45.214"

# Game window
SIZE = 3

MWIDTH = 850.0
MHEIGHT = 610.0
MENU_RESOLUTION = (MWIDTH, MHEIGHT)

#Restart button


# Player
PLAYER_COLORS = [(240, 0, 0), (0, 128, 255), (255, 255, 255)]
PLAYER_NAMES = {0: "Blue", 1: "Red"}

# About menu theme
about_theme = pygame_menu.themes.THEME_DARK.copy()
about_theme.title_font_color = (111, 222, 111)
about_theme.title_font = pmfont.FONT_BEBAS
about_theme.widget_font_size = 15  # Set the default font size
about_theme.widget_font = pmfont.FONT_COMIC_NEUE

about_text = """
Hex is a two player abstract strategy board game in
which players attempt to connect opposite sides of a
rhombus-shaped board made of hexagonal cells.

It is traditionally played on an 11×11 rhombus board,
although other board sizes are also popular. The board
is composed of hexagons called cells or hexes. Each
player is assigned a pair of opposite sides of the 
board, which they must try to connect by alternately
placing a stone of their color onto any empty hex. 
Once placed, the stones are never moved or removed.

A player wins when they successfully connect their 
sides together through a chain of adjacent stones. 
Draws are impossible in Hex due to the topology of the game board.

Despite the simplicity of its rules, the game has deep 
strategy and sharp tactics. It also has profound 
mathematical underpinnings.
"""
