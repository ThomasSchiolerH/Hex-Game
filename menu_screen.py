import os

import pygame, pygame_menu
from pygame_menu import themes
from drawboard import Board

from game import Game
from mp_game import MPGame

from ai_game_simple import SimpleAIGame
from ai_game_advanced import AdvancedAIGame

from constants import *


def show_menu():
    pygame.init()
    # Window size
    menuScreen = pygame.display.set_mode(MENU_RESOLUTION)
    # Caption of window
    pygame.display.set_caption(WINDOW_NAME)
    # Fill window background with the chosen colour
    menuScreen.fill(BACKGROUND_COLOUR)

    #HVAD GØR DET HER KODE, FORDI MAN KAN IKKE SE DET DER BLIVER SKREVET? TODO
    # Font
    #font = pygame.font.SysFont(None, 20)
    #myfont = pygame.font.SysFont("achelas.tff", 72)  # use default system font, size 10
    #mytext = myfont.render('HEX', True, (255, 100, 100))
    #menuScreen.blit(mytext, (MWIDTH * 0.45, 0))  # put the text in top left corner of screen

    # Update window
    pygame.display.flip()
    # Keep window running
    running = True

    surface = pygame.display.set_mode(MENU_RESOLUTION)

    # Menus
    def player_vs_computer_game():
        # Add your logic here for player vs computer mode
        mainmenu._open(computer_mode_menu)

    def player_vs_player_game():
        try:
            gameSize = int(boardSizeField.get_value())
            if gameSize <= 1 or gameSize > 20:
                boardSizeLabel.set_title("Board size has to be between 2-20")
            else:
                boardSize = getGameResolution(gameSize)
                gameScreen = pygame.display.set_mode(boardSize)
                gameScreen.fill(BACKGROUND_COLOUR)
                game = Game(gameScreen, gameSize)
                game.play()
        except ValueError:
            boardSizeLabel.set_title("Choose a board size")



    def start_computer_game(difficulty):
        try:
            gameSize = int(boardSizeField.get_value())
            if gameSize <= 1 or gameSize > 20:
                boardSizeLabel.set_title("Board size has to be between 2-20")
            else:
                gameSize = int(boardSizeField.get_value())
                boardSize = getGameResolution(gameSize)
                gameScreen = pygame.display.set_mode(boardSize)
                gameScreen.fill(BACKGROUND_COLOUR)
                if (difficulty == "easy"):
                    aiGame = SimpleAIGame(gameScreen, gameSize)
                elif (difficulty == "hard"):
                    aiGame = AdvancedAIGame(gameScreen, gameSize)
                aiGame.play()
        except ValueError:
            boardSizeLabel.set_title("Choose a board size")

    def getGameResolution(size):
        width = 2 * HEX_OFFSET + (1.75 * HEX_RADIUS) * size + HEX_RADIUS * size
        height = 2 * HEX_OFFSET + (1.75 * HEX_RADIUS) * size

        return (width, height)


    def about_menu():
        mainmenu._open(about)

    def host_game():
        mpgame = MPGame(menuScreen)
        mpgame.host_game()


    def join_game():
        mpgame = MPGame(menuScreen)
        mpgame.join_game()

    # Menu screens
    game_mode_menu = pygame_menu.Menu('Select Game Mode', MWIDTH, MHEIGHT, theme=themes.THEME_DARK)
    computer_mode_menu = pygame_menu.Menu('Select Difficulty', MWIDTH, MHEIGHT, theme=themes.THEME_DARK)

    # Main menu screen
    mainmenu = pygame_menu.Menu('WELCOME TO HEX', MWIDTH, MHEIGHT, theme=themes.THEME_DARK)

    # Menu buttons
    play_button = mainmenu.add.button('Play', game_mode_menu)
    host_button = mainmenu.add.button('Host', host_game)
    join_button = mainmenu.add.button('Join', join_game)
    about_button = mainmenu.add.button('About the Game', about_menu)
    quit_button = mainmenu.add.button('Quit', pygame_menu.events.EXIT)

    # Game mode menu buttons
    boardSizeLabel = game_mode_menu.add.label("Choose a board Size between 2-20")
    boardSizeField = game_mode_menu.add.text_input("")
    boardSizeField.set_border(1, WHITE)
    boardSizeField.set_padding((0, 60, 0, 60))
    boardSizeField.set_margin(0, 60)

    player_vs_player_button = game_mode_menu.add.button('Player vs Player', player_vs_player_game)
    player_vs_computer_button = game_mode_menu.add.button('Player vs Computer', player_vs_computer_game)

    # Computer Ai buttons
    easy_button = computer_mode_menu.add.button('Easy', lambda: start_computer_game('easy'))
    hard_button = computer_mode_menu.add.button('Hard', lambda: start_computer_game('hard'))


    arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))

    about = pygame_menu.Menu('About Hex', MWIDTH, MHEIGHT, theme=about_theme)
    about.add.label(about_text)

    host = pygame_menu.Menu('Host a new game', MWIDTH, MHEIGHT, theme=themes.THEME_DARK)
    join = pygame_menu.Menu('Join game', MWIDTH, MHEIGHT, theme=themes.THEME_DARK)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
        if mainmenu.is_enabled():
            mainmenu.update(events)
            mainmenu.draw(surface)

            if mainmenu.get_current().get_selected_widget():
                arrow.draw(surface, mainmenu.get_current().get_selected_widget())

        pygame.display.update()
