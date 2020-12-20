import pygame_menu


class GameMenu:
    def __init__(self, engine, screen):
        self.engine = engine
        self.screen = screen

        self.__process_func = None
        self.menu = None

        pygame_menu.themes.THEME_DARK.widget_font = pygame_menu.font.FONT_8BIT

    def set_process_func(self, func):
        self.__process_func = func

    def continue_game(self):
        self.__process_func()

    def end_game(self):
        self.engine.setup()
        self.start_menu()

    def start_like_human(self):
        self.engine.is_human = True
        self.engine.setup()
        self.__process_func()

    def start_like_agent(self):
        self.engine.is_human = False
        self.engine.setup()
        self.__process_func()

    def train_it(self):
        self.engine.is_train = True
        self.engine.setup()
        self.__process_func()

    def test_it(self):
        self.engine.is_train = False
        self.engine.setup()
        self.__process_func()

    def start_menu(self):
        self.menu = pygame_menu.Menu(300, 400, 'Dino with RL', theme=pygame_menu.themes.THEME_DARK)

        if self.engine.is_human:
            self.menu.add_button('Play', self.start_like_human)
            self.menu.add_button('AI', self.start_like_agent)

        else:
            self.menu.add_button('Play', self.start_like_agent)
            self.menu.add_button('HUMAN', self.start_like_human)
            self.menu.add_button('Train', self.train_it)
            self.menu.add_button('Test', self.test_it)

        self.menu.add_button('Exit', pygame_menu.events.EXIT)
        self.menu.mainloop(self.screen)

    def pause_menu(self):
        self.menu = pygame_menu.Menu(300, 400, 'Dino with RL', theme=pygame_menu.themes.THEME_DARK)

        self.menu.add_button('Continue', self.continue_game)
        self.menu.add_button('End Game', self.end_game)
        self.menu.add_button('Exit', pygame_menu.events.EXIT)
        self.menu.mainloop(self.screen)
