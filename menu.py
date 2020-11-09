import pygame_menu

from config import HUMAN, AGENT


class GameMenu:
    def __init__(self, game):
        self.game = game
        pygame_menu.themes.THEME_DARK.widget_font = pygame_menu.font.FONT_8BIT
        self.menu = pygame_menu.Menu(300, 400, 'Dino with RL', theme=pygame_menu.themes.THEME_DARK)

    def start_the_game(self):
        self.game.set_hero(HUMAN)
        self.game.setup()

    def start_the_ai(self):
        self.game.set_hero(AGENT)
        self.game.setup()

    def save_it(self):
        self.game.save_process()

    def load_it(self):
        self.game.load_process()

    def start_menu(self, flag=False):
        self.game.set_hero(flag)

        if not flag:
            self.menu.add_button('Play', self.start_the_game)
            self.menu.add_button('AI', self.start_the_ai)

        else:
            self.menu.add_button('Play', self.start_the_ai)
            self.menu.add_button('HUMAN', self.start_the_game)
            self.menu.add_button('Save', self.save_it)
            self.menu.add_button('Load', self.load_it)

        self.menu.add_button('Exit', pygame_menu.events.EXIT)
        self.menu.mainloop(self.game.screen)
