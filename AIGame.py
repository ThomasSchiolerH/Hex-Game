import random
import time
from game import Game

class AIGame(Game):
    def __init__(self, screen, size):
        super().__init__(screen, size)
        
        available_tiles = []

        for i in range(self.size):
            for j in range(self.size):
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

            if not self.playerTurn:
                available_tiles = []

                for i in range(self.size):
                    for j in range(self.size):
                        if self.boardMatrix[i][j] == -1:
                            available_tiles.append((i, j))

                if available_tiles:
                    i, j = random.choice(available_tiles)
                    self.boardMatrix[i][j] = int(self.playerTurn)
                    self.playerTurn = not self.playerTurn

            elif self.playerTurn:
                available_tiles = []

                for i in range(self.size):
                    for j in range(self.size):
                        if self.boardMatrix[i][j] == -1:
                            available_tiles.append((i, j))

                if available_tiles:
                    i, j = random.choice(available_tiles)
                    self.boardMatrix[i][j] = int(self.playerTurn)
                    self.playerTurn = not self.playerTurn