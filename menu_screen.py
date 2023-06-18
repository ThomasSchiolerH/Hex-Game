from pygame_menu import themes
from game import Game
from mp_game import MPGame
from ai_game_simple import SimpleAIGame
from ai_game_advanced import AdvancedAIGame
from constants import *



"""
    File By
    Author : @Marcus / SovereignPihl

"""



def show_menu():
    pygame.init()
    # Window size
    menuScreen = pygame.display.set_mode(MENU_RESOLUTION)
    # Caption of window
    pygame.display.set_caption(WINDOW_NAME)
    # Fill window background with the chosen colour
    menuScreen.fill(BACKGROUND_COLOUR)

    # Update window
    pygame.display.flip()

    surface = pygame.display.set_mode(MENU_RESOLUTION)

    # Menus
    def player_vs_computer_game():
        # Add your logic here for player vs computer mode
        mainmenu._open(computer_mode_menu)

    def player_vs_player_game(gameSize):
        gameScreen = get_game_screen(gameSize)
        game = Game(gameScreen, gameSize)
        game.play()

    def start_computer_game(difficulty, gameSize):
        gameScreen = get_game_screen(gameSize)
        if difficulty == "easy":
            aiGame = SimpleAIGame(gameScreen, gameSize)
        elif difficulty == "hard":
            aiGame = AdvancedAIGame(gameScreen, gameSize)
        aiGame.play()

    
    #    @Authors: Marcus
    def get_game_screen(gameSize):
        boardSize = getGameResolution(gameSize)
        gameScreen = pygame.display.set_mode(boardSize)
        gameScreen.fill(BACKGROUND_COLOUR)
        return gameScreen

    
    #    @Authors: Marcus
    def init_screen(mode):
        gameSize = 0
        try:
            gameSize = int(boardSizeField.get_value())
        except ValueError:
            boardSizeLabel.set_title("Choose a board size")

        if gameSize <= 1 or gameSize > 20:
            boardSizeLabel.set_title("Board size has to be between 2-20")
        else:
            if mode == "pvp":
                player_vs_player_game(gameSize)
            elif mode == "pve":
                player_vs_computer_game()
            elif mode == "host":
                host_game(gameSize)
            elif mode == "join":
                join_game(gameSize)

    def getGameResolution(size):
        width = 2 * HEX_OFFSET + (1.75 * HEX_RADIUS) * size + HEX_RADIUS * size
        height = 2 * HEX_OFFSET + (1.75 * HEX_RADIUS) * size

        return (width, height)

    def about_menu():
        mainmenu._open(about)

    
    #    @Authors: Marcus
    def host_game(size):
        gameSize = get_game_screen(size)
        mpgame = MPGame(gameSize, size)
        mpgame.host_game()

    
    #    @Authors: Marcus
    def join_game(size):
        gameSize = get_game_screen(size)
        mpgame = MPGame(gameSize, None)
        mpgame.join_game()

    # Menu screens
    game_mode_menu = pygame_menu.Menu(
        "Select Game Mode", MWIDTH, MHEIGHT, theme=themes.THEME_DARK
    )
    computer_mode_menu = pygame_menu.Menu(
        "Select Difficulty", MWIDTH, MHEIGHT, theme=themes.THEME_DARK
    )

    # Main menu screen
    mainmenu = pygame_menu.Menu(
        "WELCOME TO HEX", MWIDTH, MHEIGHT, theme=themes.THEME_DARK
    )

    # Menu buttons
    play_button = mainmenu.add.button("Play", game_mode_menu)
    about_button = mainmenu.add.button("About the Game", about_menu)
    quit_button = mainmenu.add.button("Quit", pygame_menu.events.EXIT)

    # Game mode menu buttons
    boardSizeLabel = game_mode_menu.add.label("Choose a board Size between 2- 20")
    boardSizeField = game_mode_menu.add.text_input("")
    boardSizeField.set_border(1, WHITE)
    boardSizeField.set_padding((0, 60, 0, 60))
    boardSizeField.set_margin(0, 60)

    player_vs_player_button = game_mode_menu.add.button(
        "Player vs Player", lambda: init_screen("pvp")
    )
    player_vs_computer_button = game_mode_menu.add.button(
        "Player vs Computer", lambda: init_screen("pve")
    )
    host_button = game_mode_menu.add.button("Host", lambda: init_screen("host"))
    join_button = game_mode_menu.add.button("Join", lambda: init_screen("join"))

    # Computer Ai buttons
    easy_button = computer_mode_menu.add.button(
        "Easy", lambda: start_computer_game("easy", int(boardSizeField.get_value()))
    )
    hard_button = computer_mode_menu.add.button(
        "Hard", lambda: start_computer_game("hard", int(boardSizeField.get_value()))
    )

    arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))

    about = pygame_menu.Menu("About Hex", MWIDTH, MHEIGHT, theme=about_theme)
    about.add.label(about_text)

    host = pygame_menu.Menu("Host a new game", MWIDTH, MHEIGHT, theme=themes.THEME_DARK)
    join = pygame_menu.Menu("Join game", MWIDTH, MHEIGHT, theme=themes.THEME_DARK)

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
