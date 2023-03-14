from drawboard import Board
import pygame
import sys

class Game:
    def __init__(self, boardSize: int = 6):
        self.board = Board()


    def event_handler(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    print("Quit")
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.turn()
        
        pygame.quit()
        sys.exit()

    def turn(self):
        pass

    def play(self):
        print("Playing")
        self.board.draw_board()

        pygame.display.update()
        self.board.clock.tick(30)
        self.event_handler()


