import pygame as pg
from Hero import Hero
from Env import Environment
from PhysxObj import PhysicalObject

WIDTH = 400
HEIGHT = 500


class GameEngine:
    def __init__(self):
        self.is_running = False
        self.human_player = True
        self.human = None
        self.agent = None
        # if self.human_player:
        #     self.hero = Hero()  # TODO replace Hero to Human
        # else:
        #     self.hero = Hero()  # TODO replace Hero to Agent
        self.environment = Environment()
        self.width = WIDTH
        self.height = HEIGHT
        self.screen = None
        pg.init()
        self.visible_obj = []

    def draw_obj(self, obj: PhysicalObject):
        if isinstance(obj, PhysicalObject):
            if self.screen:
                try:
                    pg.draw.rect(self.screen, (0, 128, 255),
                                 pg.Rect(obj.coord[0], obj.coord[1], obj.size[0], obj.size[1]))
                except:
                    exit(500)
            else:
                raise Exception('Screen is not initialize.')
        else:
            raise Exception('Function draw_obj can`t draw this obj.')

    def create_level(self):
        pass  # TODO create function

    def draw_visible_obj(self):
        self.visible_obj = []
        self.visible_obj.append(self.hero)
        for prop in self.environment.prop_list:
            if prop.coord[0] < self.width - prop.size[0]:
                self.visible_obj.append(prop)
        for obj in self.visible_obj:
            self.draw_obj(obj)

    def setup(self):
        self.screen = pg.display.set_mode((self.width, self.height))
        # self.draw_visible_obj()

    def update(self):
        self.hero.update()
        self.environment.update()
        self.draw_visible_obj()


def main():
    game = GameEngine()
    game.setup()


if __name__ == '__main__':
    main()
