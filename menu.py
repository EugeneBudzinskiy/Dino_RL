import pygame_menu
from config import HUMAN, AGENT
from Game import GameEngine


class GameMenu:
    def __init__(self):
        self.game = GameEngine(HUMAN)
        self.menu = pygame_menu.Menu(300, 400, 'Dino with RL', theme=pygame_menu.themes.THEME_DARK)

    def start_the_game(self):
        self.game.__init__(HUMAN)
        self.game.setup()

    def start_the_ai(self):
        self.game.__init__(AGENT)
        self.game.setup()

    def start_menu(self):
        self.menu.add_button('Play', self.start_the_game)
        self.menu.add_button('AI', self.start_the_ai)
        self.menu.add_button('Exit', pygame_menu.events.EXIT)
        self.menu.mainloop(self.game.screen)
