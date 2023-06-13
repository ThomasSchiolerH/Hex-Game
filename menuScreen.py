import os

import pygame, pygame_menu
from pygame_menu import themes
from drawboard import Board

from game import Game
from MPGame import MPGame
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


    #Menus
    def start_game():
        gameScreen = pygame.display.set_mode(GAME_RESOLUTION)
        gameScreen.fill(BACKGROUND_COLOUR)
        game = Game(gameScreen)
        game.play()

    def level_menu():
        mainmenu._open(level)

    def set_difficulty(value, difficulty):
        print(value)
        print(difficulty)

    def about_menu():
        mainmenu._open(about)

    def host_game():
        mpgame = MPGame(menuScreen)
        mpgame.host_game()


    def join_game():
        mpgame = MPGame(menuScreen)
        mpgame.join_game()


    #Main menu screen
    mainmenu = pygame_menu.Menu('WELCOME TO HEX', MWIDTH, MHEIGHT, theme=themes.THEME_DARK)

    # The rest of the buttons
    play_button = mainmenu.add.button('Play', start_game)
    host_button = mainmenu.add.button('Host', host_game)
    join_button = mainmenu.add.button('Join', join_game)
    level_button = mainmenu.add.button('Computer Level', level_menu)
    about_button = mainmenu.add.button('About the Game', about_menu)
    quit_button = mainmenu.add.button('Quit', pygame_menu.events.EXIT)

    buttons = [play_button, host_button, join_button, level_button, about_button, quit_button]

    arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))

    level = pygame_menu.Menu('Select a Difficulty', MWIDTH, MHEIGHT, theme=themes.THEME_DARK)
    level.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2), ('Medium', 3)], onchange=set_difficulty)
    arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))

    about = pygame_menu.Menu('About Hex', MWIDTH, MHEIGHT, theme=themes.THEME_DARK)
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
