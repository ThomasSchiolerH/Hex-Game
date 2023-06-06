import pygame, pygame_menu
from pygame_menu import themes

from game import Game
from menuScreenUtilities import WIDTH, HEIGHT, BACKGROUND_COLOUR, WINDOW_NAME, RESOLUTION, main_theme, difficulty_theme, about_theme, about_text


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

    #Menus
    def start_the_game():
        mainmenu._open(loading)
        pygame.time.set_timer(update_loading, 30)

    def level_menu():
        mainmenu._open(level)

    def set_difficulty(value, difficulty):
        print(value)
        print(difficulty)

    def about_menu():
        mainmenu._open(about)


    #Main menu screen
    mainmenu = pygame_menu.Menu('WELCOME TO HEX', WIDTH, HEIGHT, theme=main_theme)

    #The rest of the buttons
    play_button = mainmenu.add.button('Play', start_the_game)
    level_button = mainmenu.add.button('Computer Level', level_menu)
    about_button = mainmenu.add.button('About the Game', about_menu)
    quit_button = mainmenu.add.button('Quit', pygame_menu.events.EXIT)

    level = pygame_menu.Menu('Select a Difficulty', WIDTH, HEIGHT, theme=difficulty_theme)
    level.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2), ('Medium', 3)], onchange=set_difficulty)

    loading = pygame_menu.Menu('Loading Hex...', WIDTH, HEIGHT, theme=themes.THEME_DARK)
    loading.add.progress_bar("Progress", progressbar_id="1", default=0, width=200, )
    arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))

    about = pygame_menu.Menu('About Hex', WIDTH, HEIGHT, theme=about_theme)
    about.add.label(about_text)

    update_loading = pygame.USEREVENT + 0

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == update_loading:
                progress = loading.get_widget("1")
                progress.set_value(progress.get_value() + 1)
                if progress.get_value() == 100:
                    pygame.time.set_timer(update_loading, 0)
                    # Create an instance of the Game class
                    game = Game()
                    # Start the game by calling the play() method
                    game.play()
            if event.type == pygame.QUIT:
                exit()

        if mainmenu.is_enabled():
            mainmenu.update(events)
            mainmenu.draw(surface)
            if (mainmenu.get_current().get_selected_widget()):
                arrow.draw(surface, mainmenu.get_current().get_selected_widget())

        pygame.display.update()
