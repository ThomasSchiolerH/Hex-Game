import random
from game import Game
from constants import SIZE

class AIGame(Game):
    def __init__(self, screen):
        super().__init__(screen)
        self.playerTurn = False
        self.turn(0,0)

    def turn(self, i, j):
        if self.playerTurn:
            super().turn(i, j)
        if not self.playerTurn:
            center = int(SIZE / 2)
            if self.boardMatrix[center][center] == -1:
                self.boardMatrix[center][center] = int(self.playerTurn)
                self.playerTurn = True
            else:
                available_tiles = []
                for i in range(SIZE):
                    for j in range(SIZE):
                        if self.boardMatrix[i][j] == -1:
                            available_tiles.append((i, j))
                if available_tiles:
                    i, j = random.choice(available_tiles)
                    self.boardMatrix[i][j] = int(self.playerTurn)
                self.playerTurn = True

