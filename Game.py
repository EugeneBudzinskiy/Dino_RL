import pygame as pg
from Hero import Hero, Human
from Env import Environment
from PhysxObj import PhysicalObject
from prop import Prop, Bird, Cactus
from random import randint

WIDTH = 1200
HEIGHT = 600
BIRD_SIZE = tuple([15, 15])
CACTUS_SIZE = tuple([25, 15])


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

        self.environment = Environment()
        self.visible_obj = []

        pg.init()

    def draw_obj(self, obj):
        if isinstance(obj, Prop) or isinstance(obj, Hero):
            if self.screen:
                try:
                    cur_coord = obj.get_coord_normalized(self.height - obj.size[1])
                    pg.draw.rect(self.screen, (0, 128, 255),
                                 pg.Rect(cur_coord[0], cur_coord[1], obj.size[0], obj.size[1]))
                except:
                    exit(500)
            else:
                raise Exception('Screen is not initialize.')
        else:
            raise Exception('Function draw_obj can`t draw this obj.')

    def spawn_prop(self, last_prop: Prop):
        BIRD = 9

        distance = [50, 75, 100]
        type_prop = randint(1, 10)
        instance_prop = None
        if type_prop == BIRD:
            instance_prop = Bird(BIRD_SIZE[0], BIRD_SIZE[1])
        if type_prop != BIRD:
            instance_prop = Cactus(CACTUS_SIZE[0], CACTUS_SIZE[1])
        self.environment.spawn_prop(instance_prop, last_prop.coord[0] + last_prop.size[0] + distance[randint(0, 2)])

    def create_level(self):
        first_cactus = Cactus(CACTUS_SIZE[0], CACTUS_SIZE[1])
        self.environment.spawn_prop(first_cactus, 100)
        for props in range(0, 19):
            self.spawn_prop(self.environment.prop_list[len(self.environment.prop_list)-1])

    def draw_visible_obj(self):
        self.visible_obj = []
        # self.visible_obj.append(self.hero)
        for prop in self.environment.prop_list:
            if prop.coord[0] < self.width - prop.size[0]:
                self.visible_obj.append(prop)
        for obj in self.visible_obj:
            self.draw_obj(obj)

    def setup(self):
        self.screen = pg.display.set_mode((self.width, self.height))
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
            key_arr = [pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT]
            self.hero.change_state(pressed, key_arr)

            self.screen.fill((0, 0, 0))
            # self.hero.update()
            self.environment.update()
            if len(self.environment.prop_list) < 20:
                self.spawn_prop(self.environment.prop_list[len(self.environment.prop_list)-1])
            self.draw_visible_obj()
            pg.display.flip()

            self.clock.tick(60)


def main():
    game = GameEngine()
    game.setup()


if __name__ == '__main__':
    main()
