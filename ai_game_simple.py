import random
from game import Game
import pygame
import sys
from constants import WINCOLORS


class SimpleAIGame(Game):
    def __init__(self, screen, size):
        super().__init__(screen, size)
        self.self = self.size

        if self.size == 3:
            self.boardMatrix[1][1] = int(self.playerTurn)
            self.playerTurn = not self.playerTurn

    def turn(self, i, j):
        while True:
            if self.boardMatrix[i][j] == -1:
                self.boardMatrix[i][j] = int(self.playerTurn)
                self.playerTurn = not self.playerTurn
                break
            else:
                print("Invalid move")
                return

        if self.size == 3:
            self.three_stategy(i,j)
        else:
            if self.check_win_condition(int(not self.playerTurn)):  # Check if the opponent has won
                    print(f"Player {int(self.playerTurn)} wins!")
                    self.board.colorWinPath(self.connected, self.screen, WINCOLORS[self.playerTurn])
                    self.board.display_winner_box(self.playerTurn, self.screen)
            else:
                available_tiles = []
                for i in range(self.size):
                    for j in range(self.size):
                        if self.boardMatrix[i][j] == -1:
                            available_tiles.append((i, j))

                if available_tiles:
                    i, j = random.choice(available_tiles)
                    self.boardMatrix[i][j] = int(self.playerTurn)
                    self.playerTurn = not self.playerTurn

                    if self.check_win_condition(int(not self.playerTurn)):  # Check if the opponent has won
                        print(f"Player {int(self.playerTurn)} wins!")
                        self.board.colorWinPath(self.connected, self.screen, WINCOLORS[self.playerTurn])
                        self.board.display_winner_box(self.playerTurn, self.screen)

    def three_stategy(self, i, j):
        # Check if the player move is a corner move
        if (i, j) in [(0, 0), (0, self.size-1), (self.size-1, 0), (self.size-1, self.size-1)]:
            if i == 0:  # Left corners
                if self.boardMatrix[i][1] == -1:
                    self.boardMatrix[i][1] = int(self.playerTurn)
                else:
                    while True:
                        i, j = random.randint(0, self.size-1), random.randint(0, self.size-1)
                        if self.boardMatrix[i][j] == -1:
                            self.boardMatrix[i][j] = int(self.playerTurn)
                            break
            elif i == self.size-1:  # Right corners
                if self.boardMatrix[i][1] == -1:
                    self.boardMatrix[i][1] = int(self.playerTurn)
                else:
                    while True:
                        i, j = random.randint(0, self.size-1), random.randint(0, self.size-1)
                        if self.boardMatrix[i][j] == -1:
                            self.boardMatrix[i][j] = int(self.playerTurn)
                            break
        # Check if the player move is a right or left edge move
        elif (i,j) in [(0, 1), (self.size-1, 1), (1, 0), (1, self.size-1)]:
            if i == 0:
                if self.boardMatrix[i][self.size-1] == -1:
                    self.boardMatrix[i][self.size-1] = int(self.playerTurn)
                else:
                    while True:
                        i, j = random.randint(0, self.size-1), random.randint(0, self.size-1)
                        if self.boardMatrix[i][j] == -1:
                            self.boardMatrix[i][j] = int(self.playerTurn)
                            break
            elif i == self.size-1:
                if self.boardMatrix[i][0] == -1:
                    self.boardMatrix[i][0] = int(self.playerTurn)
                else:
                    while True:
                        i, j = random.randint(0, self.size-1), random.randint(0, self.size-1)
                        if self.boardMatrix[i][j] == -1:
                            self.boardMatrix[i][j] = int(self.playerTurn)
                            break
            elif j == 0:
                if self.boardMatrix[self.size-1][j] == -1:
                    self.boardMatrix[self.size-1][j] = int(self.playerTurn)
                else:
                    while True:
                        i, j = random.randint(0, self.size-1), random.randint(0, self.size-1)
                        if self.boardMatrix[i][j] == -1:
                            self.boardMatrix[i][j] = int(self.playerTurn)
                            break
            elif j == self.size-1:
                if self.boardMatrix[0][j] == -1:
                    self.boardMatrix[0][j] = int(self.playerTurn)
                else:
                    while True:
                        i, j = random.randint(0, self.size-1), random.randint(0, self.size-1)
                        if self.boardMatrix[i][j] == -1:
                            self.boardMatrix[i][j] = int(self.playerTurn)
                            break
        # Check if the player move is a top or bottom edge move
        elif (i,j) in [(1, 0), (1, self.size-1)]:
            adjacent_tiles = []
            if j == 0:
                if self.boardMatrix[0][1] == -1:
                    self.boardMatrix[0][1] = int(self.playerTurn)
                else:
                    adjacent_tiles.append((0, 1))
            elif j == self.size-1:
                if self.boardMatrix[self.size-1][1] == -1:
                    self.boardMatrix[self.size-1][1] = int(self.playerTurn)
                else:
                    adjacent_tiles.append((self.size-1, 1))

            if adjacent_tiles:
                while True:
                    i, j = random.choice(adjacent_tiles)
                    if self.boardMatrix[i][j] == -1:
                        self.boardMatrix[i][j] = int(self.playerTurn)
                        break
        else:
            self.boardMatrix[i][j] = int(self.playerTurn)
        self.playerTurn = not self.playerTurn
