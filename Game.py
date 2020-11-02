import pygame as pg
from Hero import Human
from Env import Environment
from config import *
from Graphics import Graphics


class GameEngine:
    def __init__(self):
        self.is_running = False
        self.human_player = True

        self.human = None
        self.agent = None
        self.clock = None
        self.screen = None

        self.width = WIDTH
        self.height = HEIGHT

        if self.human_player:
            self.hero = Human()  # TODO replace Hero to Human
        else:
            self.hero = None  # TODO replace Hero to Agent
        self.graphics = None
        self.environment = Environment()
        self.visible_obj = []

        pg.init()

    def create_level(self):
        self.environment.spawn_prop(FIRST_SPAWN_DISTANCE)
        for props in range(0, NUMBER_OF_EXISTING_PROP):
            self.environment.spawn_prop()

    def draw_visible_obj(self):
        self.visible_obj = []
        self.visible_obj.append(self.hero)
        for prop in self.environment.prop_list:
            if prop.coord[0] < self.width - prop.size[0]:
                self.visible_obj.append(prop)
        for obj in self.visible_obj:
            self.graphics.draw_obj(obj)

    def setup(self):
        self.screen = pg.display.set_mode((self.width, self.height))
        self.graphics = Graphics(self.screen)
        self.create_level()

        self.clock = pg.time.Clock()

        self.is_running = True
        self.update()

    def update(self):
        while self.is_running:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.is_running = False

            pressed = pg.key.get_pressed()
            key_arr = [pg.K_UP, pg.K_DOWN]
            self.hero.change_state(pressed, key_arr)

            self.screen.fill((0, 0, 0))
            self.hero.update()
            self.environment.update()

            self.draw_visible_obj()
            pg.display.flip()

            self.clock.tick(FPS)
