from math import dist
import socket
from constants import *
from sys import argv

from drawboard import Board
import pygame
import sys


class MPGame:
    def __init__(self, screen):
        self.board = Board(SIZE)
        self.clock = pygame.time.Clock()
        self.playerTurn = False
        self.screen = screen
        self.boardMatrix = [[-1 for i in range(SIZE)] for j in range(SIZE)]
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host = None

    def event_handler(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    print("Quit")
                if event.type == pygame.MOUSEBUTTONDOWN and self.playerTurn:
                    self.local_turn()

            if not self.playerTurn:
                self.recieve_turn()

        pygame.quit()
        sys.exit()

    def turn(self, i, j):
        if self.boardMatrix[i][j] == -1:
            self.boardMatrix[i][j] = int(self.playerTurn)
            self.playerTurn = not self.playerTurn
            self.board.draw_board(self.boardMatrix, self.screen)

    def get_host(self):
        font = pygame.font.Font(None, 32)
        input_box = pygame.Rect(100, 100, 140, 32)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = "localhost:9000"
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            host, port = text.split(":")
                            return host, int(port)
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            self.screen.fill(BACKGROUND_COLOUR)
            # Render the current text.
            txt_surface = font.render(text, True, color)
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width
            # Blit the text.
            self.screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            # Blit the input_box rect.
            pygame.draw.rect(self.screen, color, input_box, 2)

            pygame.display.flip()
            self.clock.tick(30)

    def host_game(self):
        self.screen.fill(BACKGROUND_COLOUR)
        pygame.display.update()
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        print(IPAddr)
        self.socket.bind(("localhost", 9000))
        print("awaiting other player")
        _, self.host = self.socket.recvfrom(4)

        print(self.host)

        self.playerTurn = True
        self.board.draw_board(self.boardMatrix, self.screen)
        self.clock.tick(30)
        self.event_handler()

    def join_game(self):
        self.socket.bind(("localhost", 9001))
        self.host = self.get_host()
        self.socket.sendto(bytes("join", "utf-8"), self.host)

        self.board.draw_board(self.boardMatrix, self.screen)

        self.clock.tick(30)
        self.event_handler()

    def recieve_turn(self):
        m, _ = self.socket.recvfrom(5)
        m = m.decode("utf-8", "strict")
        print(m)
        i, j = m.split(",")
        self.turn(int(i), int(j))

    def local_turn(self):
        pos = self.board.get_neareast_pos(*pygame.mouse.get_pos())
        if pos is not None:
            print("{},{}".format(*pos))
            self.turn(*pos)
            self.socket.sendto(bytes("{},{}".format(*pos), "utf-8"), self.host)

