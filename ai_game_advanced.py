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
                            score = self.alpha_beta_pruned_minimax(3, False, float('-inf'), float('inf'))
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

        # Visited tiles stored in 2d list - use DFS so no tiles are visited twice
        visited = [[False for _ in range(self.size)] for _ in range(self.size)]  # Set all false to start
        for i in range(self.size):
            if player == 0:
                if self.boardMatrix[i][start_side] == player:  # Check if the tile is occupied by player 1
                    if self.dfs(i, start_side, player, visited, set()):  # DFS from current tile
                        return True  # Player has won
            elif player == 1:
                if self.boardMatrix[start_side][i] == player:
                    if self.dfs(start_side, i, player, visited, set()):
                        return True

        return False

    # All possible ways to place connecting tile
    NEIGHBOR_OFFSETS = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, 1), (1, -1)]

    def dfs(self, i, j, player, visited, connected):
        # Check out of bounds
        if i < 0 or i >= self.size or j < 0 or j >= self.size or self.boardMatrix[i][j] != player or visited[i][j]:
            return False

        # Mark current tile as visited
        visited[i][j] = True
        connected.add((i, j))

        if player == 0 and j == self.size - 1:  # Blue player and rightmost tile
            return True
        elif player == 1 and i == self.size - 1:  # Red player and bottommost tile
            return True

        for dx, dy in self.NEIGHBOR_OFFSETS:
            ni, nj = i + dx, j + dy
            if self.dfs(ni, nj, player, visited, connected):  # dfs from each neighbor tile
                return True  # A win has been found

        return False

    def alpha_beta_pruned_minimax(self, depth, maximizingPlayer, alpha, beta):
        if depth == 0 or self.check_win_condition(0) or self.check_win_condition(1):
            return self.evaluate()

        if maximizingPlayer:
            best_score = float('-inf')
            for i in range(self.size):
                for j in range(self.size):
                    if self.boardMatrix[i][j] == -1:
                        self.boardMatrix[i][j] = 1
                        score = self.alpha_beta_pruned_minimax(depth - 1, False, alpha, beta)
                        self.boardMatrix[i][j] = -1
                        best_score = max(best_score, score)
                        alpha = max(alpha, best_score)
                        if beta <= alpha:
                            break
            return best_score
        else:
            best_score = float('inf')
            for i in range(self.size):
                for j in range(self.size):
                    if self.boardMatrix[i][j] == -1:
                        self.boardMatrix[i][j] = 0
                        score = self.alpha_beta_pruned_minimax(depth - 1, True, alpha, beta)
                        self.boardMatrix[i][j] = -1
                        best_score = min(best_score, score)
                        beta = min(beta, best_score)
                        if beta <= alpha:
                            break
            return best_score

    def evaluate(self):
        score = 0
        for i in range(self.size):
            # Check rows
            if all(self.boardMatrix[i][j] == 1 for j in range(self.size)):
                score += 100  # Increased weight for horizontal paths
            elif all(self.boardMatrix[i][j] == 0 for j in range(self.size)):
                score -= 100  # Increased weight for horizontal paths

            # Check columns
            if all(self.boardMatrix[j][i] == 1 for j in range(self.size)):
                score += 10
            elif all(self.boardMatrix[j][i] == 0 for j in range(self.size)):
                score -= 10

        # Check diagonals
        if all(self.boardMatrix[i][i] == 1 for i in range(self.size)):
            score += 10
        elif all(self.boardMatrix[i][i] == 0 for i in range(self.size)):
            score -= 10

        if all(self.boardMatrix[i][self.size - i - 1] == 1 for i in range(self.size)):
            score += 10
        elif all(self.boardMatrix[i][self.size - i - 1] == 0 for i in range(self.size)):
            score -= 10

        return score