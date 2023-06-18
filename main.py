import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
os.environ['SDL_VIDEO_CENTERED'] = '1'

import pygame
import menu_screen


def main():
    pygame.init()
    pygame.display.set_caption("Hex")
    menu_screen.show_menu()


if __name__ == "__main__":
    main()