from pygame import mouse

from constants import *
from drawboard import Board
import pygame
import sys

from main import main


class Game:
    def __init__(self, screen, size):
        self.size = size
        self.gametype = None
        self.board = Board(self.size)
        self.clock = pygame.time.Clock()
        self.playerTurn = True
        self.screen = screen
        self.connected = []
        self.boardMatrix = [[-1 for _ in range(size)] for _ in range(size)]
        self.restartButton = pygame.Rect(10, 10, 100, 40)
        self.menuButton = pygame.Rect(120, 10, 100, 40)

    def event_handler(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    print("Quit")

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = self.board.get_nearest_pos(*pygame.mouse.get_pos())
                    if pos is not None:
                        self.turn(*pos)
                        self.board.draw_board(self.boardMatrix, self.screen)
                        # Check if the current player has won
                        if self.check_win_condition(int(not self.playerTurn)):
                            print(f"Player {int(self.playerTurn)} wins!")
                            self.board.colorWinPath(self.connected, self.screen, WINCOLORS[self.playerTurn])
                            self.board.display_winner_box(self.playerTurn, self.screen)
                    # Check if restart button is clicked
                    if self.restartButton.collidepoint(event.pos):
                        self.restart_game()
                    if self.menuButton.collidepoint(event.pos):
                        self.backToMenu()
                #Press R to restart
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.restart_game()

            if self.restartButton.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, LIGHT_GREY, self.restartButton)
            else:
                pygame.draw.rect(self.screen, DARK_GREY, self.restartButton)

            if self.menuButton.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, LIGHT_GREY, self.menuButton)
            else:
                pygame.draw.rect(self.screen, DARK_GREY, self.menuButton)

            self.drawbuttons()
            pygame.display.update()

        pygame.quit()
        sys.exit(0)


    def restart_game(self):
        self.boardMatrix = [[-1 for _ in range(self.size)] for _ in range(self.size)]
        if (self.gametype == "AiGame"):
            self.playerTurn = False
            self.boardMatrix[1][1] = 1
        else:
            self.playerTurn = True

        self.board.draw_board(self.boardMatrix, self.screen)  # Redraw the game board



    def turn(self, i, j):
        if self.boardMatrix[i][j] == -1:
            self.boardMatrix[i][j] = int(self.playerTurn)
            self.playerTurn = not self.playerTurn


    def check_win_condition(self, player):
        # Set boundaries for dfs
        if player == 0:
            start_side, end_side = 0, self.size - 1
        elif player == 1:
            start_side, end_side = 0, self.size - 1
        else:
            return False

        #Visited tiles stored in 2d list - use DFS so no tiles are visited twice
        visited = [[False for _ in range(self.size)] for _ in range(self.size)] # Set all false to start
        for i in range(self.size):
            if player == 0:
                if self.boardMatrix[i][start_side] == player: # Check if the tile is occupied by player 1
                    if self.dfs(i, start_side, player, visited, []): # DFS from current tile
                        return True # Player has won
            elif player == 1:
                if self.boardMatrix[start_side][i] == player:
                    if self.dfs(start_side, i, player, visited, []):
                        return True

        return False

    # All possible ways to place connecting tile
    NEIGHBOR_OFFSETS = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, 1), (1, -1)]
    def dfs(self, i, j, player, visited, path):

        # Check out of bounds
        if i < 0 or i >= self.size or j < 0 or j >= self.size or self.boardMatrix[i][j] != player or visited[i][j]:
            return False

        # Mark current tile as visited
        visited[i][j] = True
        path.append((i, j))


        if player == 0 and j == self.size - 1: # Blue player and right most tile
            return True
        elif player == 1 and i == self.size - 1: # Red player and bottom must tile
            return True

        for dx, dy in self.NEIGHBOR_OFFSETS:
            ni, nj = i + dx, j + dy
            if self.dfs(ni, nj, player, visited, path): # dfs from each neighbor tile
                self.connected = path
                return True # A win has been found

        path.pop()

        return False

    def drawbuttons(self):
        text = pygame.font.SysFont('Corbel', 35).render("Restart", True, WHITE)
        self.screen.blit(text,
                         (self.restartButton.centerx - text.get_width() // 2,
                          self.restartButton.centery - text.get_height() // 2))
        text = pygame.font.SysFont('Corbel', 35).render("Menu", True, WHITE)
        self.screen.blit(text,
                         (self.menuButton.centerx - text.get_width() // 2,
                          self.menuButton.centery - text.get_height() // 2))

    def play(self):
        print("Playing")
        self.board.draw_board(self.boardMatrix, self.screen)

        pygame.display.update()
        self.clock.tick(30)
        self.event_handler()

    def backToMenu(self):
        main()



