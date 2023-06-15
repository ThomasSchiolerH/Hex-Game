import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from game import Game
import pygame
from menu_screen import show_menu
import os


def main():
    pygame.init()
    pygame.display.set_caption("Hex")
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    show_menu()


if __name__ == "__main__":
    main()