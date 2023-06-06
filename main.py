from game import Game
import pygame, numpy

from menuScreen import show_menu


def main():
    pygame.init()
    pygame.display.set_caption("Hex")
    show_menu()
if __name__ == "__main__":
    main()