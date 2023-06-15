from constants import SIZE, BACKGROUND_COLOUR, GAME_RESOLUTION
from drawboard import Board
import pygame
import sys

class Game:
    def __init__(self, screen):
        self.board = Board(SIZE)
        self.clock = pygame.time.Clock()
        self.playerTurn = True
        self.screen = screen
        self.boardMatrix = [[-1 for _ in range(SIZE)] for _ in range(SIZE)]
        self.winner = None  # Winner attribute to store the winning player
        self.winner_found = False  # Flag to indicate if a winner is found

    def display_winner_box(self, winner):
        # Create a font and render the winner text
        font = pygame.font.Font(None, 48)
        if winner == 0:
            text = font.render(f"Blue Player wins!", True, (255, 255, 255))
        else:
            text = font.render(f"Red Player wins!", True, (255, 255, 255))

        # Calculate the dimensions and position of the box
        box_width = text.get_width() + 20
        box_height = text.get_height() + 20
        box_x = (GAME_RESOLUTION[0] - box_width) // 2
        box_y = (GAME_RESOLUTION[1] - box_height) // 2

        # Create a transparent surface for the box
        box_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
        border_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
        text_surface = pygame.Surface(text.get_size(), pygame.SRCALPHA)

        # Set the desired transparency (here, 128 for 50% transparency)
        alpha_value = 128

        # Fill the surfaces with the desired transparency
        box_surface.fill((0, 0, 0, alpha_value))
        border_surface.fill((255, 255, 255, alpha_value))
        text_surface.fill((255, 255, 255, alpha_value))

        # Draw the border onto the box surface
        pygame.draw.rect(box_surface, (255, 255, 255, alpha_value), (0, 0, box_width, box_height), 2)

        # Blit the box, border, and text onto the screen
        self.screen.blit(box_surface, (box_x, box_y))
        self.screen.blit(border_surface, (box_x, box_y))
        self.screen.blit(text, (box_x + 10, box_y + 10))

        pygame.display.flip()

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
                            self.winner = int(self.playerTurn)
                            self.winner_found = True
                            self.display_winner_box(self.winner)

            pygame.display.update()  # Update the display

        pygame.quit()
        sys.exit(0)

    def turn(self, i, j):
        if self.boardMatrix[i][j] == -1:
            self.boardMatrix[i][j] = int(self.playerTurn) # integer 0 or 1 depending on turn - update matrix
            self.playerTurn = not self.playerTurn #Switch between true and false

    def check_win_condition(self, player):
        # Check if valid player and give player side
        if player == 0:  # Blue player
            start_side, end_side = 0, SIZE - 1
        elif player == 1:  # Red player
            start_side, end_side = 0, SIZE - 1
        else:
            return False

        #Visited tiles stored in 2d list - use DFS so no tiles are visited twice
        visited = [[False for _ in range(SIZE)] for _ in range(SIZE)] # Set all false to start
        for i in range(SIZE):
            if player == 0:
                if self.boardMatrix[i][start_side] == player: # Check if the tile is occupied by player 1
                    if self.dfs(i, start_side, player, visited, set()): # DFS from current tile
                        return True # Player has won
            elif player == 1:
                if self.boardMatrix[start_side][i] == player:
                    if self.dfs(start_side, i, player, visited, set()):
                        return True

        return False

    # All possible ways to place connecting tile
    NEIGHBOR_OFFSETS = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, 1), (1, -1)]
    def dfs(self, i, j, player, visited, connected):
        # Check out of bounds
        if i < 0 or i >= SIZE or j < 0 or j >= SIZE or self.boardMatrix[i][j] != player or visited[i][j]:
            return False

        # Mark current tile as visited
        visited[i][j] = True
        connected.add((i, j))

        if player == 0 and j == SIZE - 1: # Blue player and rightmost tile
            return True
        elif player == 1 and i == SIZE - 1: # Red player and bottom-most tile
            return True

        for dx, dy in self.NEIGHBOR_OFFSETS:
            ni, nj = i + dx, j + dy
            if self.dfs(ni, nj, player, visited, connected): # dfs from each neighboring tile
                return True # A win has been found

        return False

    def play(self):
        print("Playing")
        self.board.draw_board(self.boardMatrix, self.screen)

        pygame.display.update()
        self.clock.tick(30)
        self.event_handler()
