import random
import time
from game import Game
from constants import SIZE

class AIGame(Game):
    def __init__(self, screen):
        super().__init__(screen)
        available_tiles = []
        for i in range(SIZE):
            for j in range(SIZE):
                if self.boardMatrix[i][j] == -1:
                    available_tiles.append((i, j))

        if available_tiles:
            i, j = random.choice(available_tiles)
            self.boardMatrix[i][j] = int(self.playerTurn)
            self.playerTurn = not self.playerTurn

    def turn(self, i, j):
        if self.boardMatrix[i][j] == -1:
            self.boardMatrix[i][j] = int(self.playerTurn)
            self.playerTurn = not self.playerTurn

            if self.check_win_condition(
                    int(not self.playerTurn)):  # Check if current player has won - uses opposite player
                print(f"Player {int(self.playerTurn)} wins!")

            if not self.playerTurn:
                available_tiles = []
                for i in range(SIZE):
                    for j in range(SIZE):
                        if self.boardMatrix[i][j] == -1:
                            available_tiles.append((i, j))
                if available_tiles:
                    i, j = random.choice(available_tiles)
                    self.boardMatrix[i][j] = int(self.playerTurn)
                    self.playerTurn = not self.playerTurn
            elif self.playerTurn:
                available_tiles = []
                for i in range(SIZE):
                    for j in range(SIZE):
                        if self.boardMatrix[i][j] == -1:
                            available_tiles.append((i, j))
                if available_tiles:
                    i, j = random.choice(available_tiles)
                    self.boardMatrix[i][j] = int(self.playerTurn)
                    self.playerTurn = not self.playerTurn