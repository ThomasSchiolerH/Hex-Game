import pygame, pygame_menu
from pygame_menu import themes
from drawboard import Board

from game import Game
from MPGame import MPGame
from AIGame import AIGame
from constants import *


def show_menu():
    pygame.init()
    # Window size
    screen = pygame.display.set_mode(RESOLUTION)
    # Caption of window
    pygame.display.set_caption(WINDOW_NAME)
    # Fill window background with the chosen colour
    screen.fill(BACKGROUND_COLOUR)
    # Font
    font = pygame.font.SysFont(None, 20)

    myfont = pygame.font.SysFont("achelas.tff", 72)  # use default system font, size 10
    mytext = myfont.render('HEX', True, (255, 100, 100))
    screen.blit(mytext, (WIDTH * 0.45, 0))  # put the text in top left corner of screen

    # Update window
    pygame.display.flip()
    # Keep window running
    running = True

    surface = pygame.display.set_mode((WIDTH, HEIGHT))

    # Menus
    def start_game():
        main_menu._open(game_mode_menu)

    """
    def level_menu():
        main_menu._open(game_mode_menu)
    """

    def player_vs_player_game():
        game = Game(screen)
        game.play()

    def player_vs_computer_game():
        # Add your logic here for player vs computer mode
        print("Not yet implemented")
        main_menu._open(computer_mode_menu)
        pass

    """
    def set_difficulty(value, difficulty):
        print(value)
        print(difficulty)
    """
    def start_computer_game(difficulty):
        # Set the game mode
        game_mode = "computer"
        # Start the game
        game = Game(screen)
        game.set_game_mode(game_mode)
        game.play()

    def about_menu():
        main_menu._open(about)

    def host_game():
        mpgame = MPGame(screen)
        mpgame.host_game()

    def join_game():
        mpgame = MPGame(screen)
        mpgame.join_game()
    
    def test_ai_game():
        ai_game = AIGame(screen)
        ai_game.play()

    # Menu screens

    main_menu = pygame_menu.Menu('Welcome to Hex', WIDTH, HEIGHT, theme=themes.THEME_DARK)
    game_mode_menu = pygame_menu.Menu('Select Game Mode', WIDTH, HEIGHT, theme=themes.THEME_DARK)
    computer_mode_menu = pygame_menu.Menu('Select Difficulty', WIDTH, HEIGHT, theme=themes.THEME_DARK)

    # Main menu buttons

    play_button = main_menu.add.button('Play', start_game)
    host_button = main_menu.add.button('Host', host_game)
    join_button = main_menu.add.button('Join', join_game)
    # level_button = main_menu.add.button('Computer Level', level_menu)
    about_button = main_menu.add.button('About the Game', about_menu)
    quit_button = main_menu.add.button('Quit', pygame_menu.events.EXIT)

    # Game mode menu buttons

    player_vs_player_button = game_mode_menu.add.button('Player vs Player', player_vs_player_game)
    player_vs_computer_button = game_mode_menu.add.button('Player vs Computer', player_vs_computer_game)
    back_button = game_mode_menu.add.button('Back', pygame_menu.events.BACK)

    # Computer game menu buttons

    test_ai_button = main_menu.add.button('Test AI Game', test_ai_game)


    easy_button = computer_mode_menu.add.button('Easy', lambda: start_computer_game('easy'))
    medium_button = computer_mode_menu.add.button('Medium', lambda: player_vs_computer_game('medium'))
    hard_button = computer_mode_menu.add.button('Hard', lambda: player_vs_computer_game('hard'))
    back_button = computer_mode_menu.add.button('Back', pygame_menu.events.BACK)

    # level = pygame_menu.Menu('Select a Difficulty', WIDTH, HEIGHT, theme=themes.THEME_DARK)
    # level.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2), ('Medium', 3)], onchange=set_difficulty)
    arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))

    about = pygame_menu.Menu('About Hex', WIDTH, HEIGHT, theme=themes.THEME_DARK)
    about.add.label(about_text)

    host = pygame_menu.Menu('Host a new game', WIDTH, HEIGHT, theme=themes.THEME_DARK)

    join = pygame_menu.Menu('Join game', WIDTH, HEIGHT, theme=themes.THEME_DARK)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
        if main_menu.is_enabled():
            main_menu.update(events)
            main_menu.draw(surface)
            if main_menu.get_current().get_selected_widget():
                arrow.draw(surface, main_menu.get_current().get_selected_widget())

        pygame.display.update()
