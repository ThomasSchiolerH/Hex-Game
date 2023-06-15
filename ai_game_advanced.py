import random
import time
from game import Game


class AdvancedAIGame(Game):
    def __init__(self, screen, size):
        super().__init__(screen, size)
        self.self = size
        if self.size == 3:
            self.boardMatrix[1][1] = int(self.playerTurn)
            self.playerTurn = not self.playerTurn
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
                best_score = float('-inf')
                best_move = None
                for i in range(self.size):
                    for j in range(self.size):
                        if self.boardMatrix[i][j] == -1:
                            self.boardMatrix[i][j] = int(self.playerTurn)
                            score = self.minimax(3, False)
                            self.boardMatrix[i][j] = -1
                            if score > best_score:
                                best_score = score
                                best_move = (i, j)
                if best_move:
                    i, j = best_move
                    self.boardMatrix[i][j] = int(self.playerTurn)
                    self.playerTurn = not self.playerTurn

            # Check if the current player has won
            if self.check_win_condition(int(not self.playerTurn)):
                print(f"Player {int(self.playerTurn)} wins!")

    def check_win_condition(self, player):
        # Check if valid player and give player side
        if player == 0:  # Blue player
            start_side, end_side = 0, self.size - 1
        elif player == 1:  # Red player
            start_side, end_side = 0, self.size - 1
        else:
            return False

        #Visited tiles stored in 2d list - use DFS so no tiles are visited twice
        visited = [[False for _ in range(self.size)] for _ in range(self.size)] # Set all false to start
        for i in range(self.size):
            if player == 0:
                if self.boardMatrix[i][start_side] == player: # Check if the tile is occupied by player 1
                    if self.dfs(i, start_side, player, visited, set()): # DFS from current tile
                        return True # Player has won
            elif player == 1:
                if self.boardMatrix[start_side][i] == player:
                    if self.dfs(start_side, i, player, visited, set()):
                        return True

        return False

    # All possible ways to palce connecting tile
    NEIGHBOR_OFFSETS = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, 1), (1, -1)]
    def dfs(self, i, j, player, visited, connected):
        # Check out of bounds
        if i < 0 or i >= self.size or j < 0 or j >= self.size or self.boardMatrix[i][j] != player or visited[i][j]:
            return False

        # Mark current tile as visited
        visited[i][j] = True
        connected.add((i, j))

        if player == 0 and j == self.size - 1: # Blue player and right most tile
            return True
        elif player == 1 and i == self.size - 1: # Red player and bottom must tile
            return True

        for dx, dy in self.NEIGHBOR_OFFSETS:
            ni, nj = i + dx, j + dy
            if self.dfs(ni, nj, player, visited, connected): # dfs from each neighbor tile
                return True # A win ahs been found

        return False

    def minimax(self, depth, maximizingPlayer):
        if depth == 0 or self.check_win_condition(0) or self.check_win_condition(1):
            return self.evaluate()

        if maximizingPlayer:
            maxEval = float('-inf')
            for i in range(self.size):
                for j in range(self.size):
                    if self.boardMatrix[i][j] == -1:
                        self.boardMatrix[i][j] = 1
                        eval = self.minimax(depth - 1, False)
                        self.boardMatrix[i][j] = -1
                        maxEval = max(maxEval, eval)
            return maxEval
        else:
            minEval = float('inf')
            for i in range(self.size):
                for j in range(self.size):
                    if self.boardMatrix[i][j] == -1:
                        self.boardMatrix[i][j] = 0
                        eval = self.minimax(depth - 1, True)
                        self.boardMatrix[i][j] = -1
                        minEval = min(minEval, eval)
            return minEval

    def evaluate(self):
        score = 0
        # Check rows
        for i in range(self.size):
            if self.boardMatrix[i][0] == self.boardMatrix[i][1] == self.boardMatrix[i][2] == 1:
                score += 10
            elif self.boardMatrix[i][0] == self.boardMatrix[i][1] == self.boardMatrix[i][2] == 0:
                score -= 10

        # Check columns
        for j in range(self.size):
            if self.boardMatrix[0][j] == self.boardMatrix[1][j] == self.boardMatrix[2][j] == 1:
                score += 10
            elif self.boardMatrix[0][j] == self.boardMatrix[1][j] == self.boardMatrix[2][j] == 0:
                score -= 10

        # Check diagonals
        if self.boardMatrix[0][0] == self.boardMatrix[1][1] == self.boardMatrix[2][2] == 1:
            score += 10
        elif self.boardMatrix[0][0] == self.boardMatrix[1][1] == self.boardMatrix[2][2] == 0:
            score -= 10
        if self.boardMatrix[0][2] == self.boardMatrix[1][1] == self.boardMatrix[2][0] == 1:
            score += 10
        elif self.boardMatrix[0][2] == self.boardMatrix[1][1] == self.boardMatrix[2][0] == 0:
            score -= 10

        return score