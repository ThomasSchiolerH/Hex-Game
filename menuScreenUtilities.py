#Constants
import pygame_menu, pygame_menu.font as pmfont

WIDTH = (800)
HEIGHT = (800)
RESOLUTION = (WIDTH,HEIGHT)
ROWS, COLS = 11,11
HEXAGON_size = WIDTH//COLS

#Game Window Name
WINDOW_NAME = "HEX BOARD GAME"

#Colours
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0, 255, 0)
BACKGROUND_COLOUR = WHITE

#Main menu theme
main_theme = pygame_menu.themes.THEME_DARK.copy()
main_theme.title_font_color = (111, 222, 111)
main_theme.title_font = pmfont.FONT_BEBAS

#Difficulty menu theme
difficulty_theme = pygame_menu.themes.THEME_DARK.copy()
difficulty_theme.title_font_color = (111, 222, 111)
difficulty_theme.title_font = pmfont.FONT_BEBAS

#About menu theme
about_theme = pygame_menu.themes.THEME_DARK.copy()
about_theme.title_font_color = (111, 222, 111)
about_theme.title_font = pmfont.FONT_BEBAS
about_theme.widget_font_size = 15  # Set the default font size
about_theme.widget_font = pmfont.FONT_COMIC_NEUE

#About text for the about menu
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