from game import Game
import pygame

def main():
    pygame.init()
    pygame.display.set_caption("Hex")
    game = Game()
    #Start the game
    game.play()

if __name__ == "__main__":
    main()