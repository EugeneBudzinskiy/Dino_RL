from CollisionLogic import CollisionLogic
from Env import Environment
from Graphics import Graphics
from Hero import Human, Hero, Agent
from config import *
from prop import Cactus, Bird
import pygame_menu as pgm
from menu import GameMenu


class GameEngine:
    def __init__(self, mode):
        self.is_running = False

        self.animation_counter = 0
        self.waiter_counter = 0
        self.score = 0

        self.clock = None
        self.width = WIDTH
        self.height = HEIGHT

        if mode == HUMAN:
            self.hero = Human()
            self.is_human = True
        else:
            self.hero = Agent()
            self.is_human = False

        self.visible_obj = []
        self.screen = pg.display.set_mode((self.width, self.height))

        self.environment = Environment()
        self.graphics = Graphics(self.screen)

        pg.init()

    def create_level(self):
        self.environment.spawn_prop(FIRST_SPAWN_DISTANCE)
        for props in range(0, NUMBER_OF_EXISTING_PROP):
            self.environment.spawn_prop()

    def continue_game(self):
        self.update()

    @staticmethod
    def back_to_main_menu():
        menu = GameMenu(GameEngine(HUMAN))
        menu.start_menu()

    def pause_menu(self):
        menu = pgm.Menu(300, 400, 'Pause', theme=pgm.themes.THEME_DARK)
        menu.add_button('Continue', self.continue_game)
        menu.add_button('Back to main menu', self.back_to_main_menu)
        menu.add_button('Exit', pgm.events.EXIT)
        menu.mainloop(self.screen)

    def draw_visible_obj(self):
        self.visible_obj = []
        self.visible_obj.append(self.hero)

        for prop in self.environment.prop_list:
            if prop.coord[0] < self.width - prop.size[0]:
                self.visible_obj.append(prop)

        for obj in self.visible_obj:
            if isinstance(self.hero, Agent):
                self.graphics.draw_obj_without_image(obj)
            elif isinstance(obj, Hero):
                self.graphics.draw_obj(obj, (self.animation_counter // 5) % 6)
            elif isinstance(obj, Cactus):
                if not obj.is_visible:
                    obj.make_visible()
                self.graphics.draw_obj(obj, 0)
            elif isinstance(obj, Bird):
                if not obj.is_visible:
                    obj.make_visible()
                self.graphics.draw_obj(obj, (self.animation_counter // 12) % 2)

    def setup(self):
        self.create_level()
        self.clock = pg.time.Clock()

        self.is_running = True
        self.update()

    def key_checker(self):
        if isinstance(self.hero, Human):
            pressed = pg.key.get_pressed()
            key_arr = [pg.K_UP, pg.K_SPACE, pg.K_DOWN, pg.K_LCTRL]
            self.hero.change_state(pressed, key_arr)

    def collision_stuff(self):
        col_log = CollisionLogic()

        cur_prop = self.environment.prop_list[0]

        return col_log.check_collision(self.hero, cur_prop)

    def update(self):
        while self.is_running or self.waiter_counter <= FPS * 4:
            self.graphics.draw_background(self.animation_counter, isinstance(self.hero, Human))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.is_running = False
                    self.waiter_counter = FPS * 4

            if self.collision_stuff():
                self.is_running = False

            self.graphics.draw_text("Score:{}".format(self.score), (980, 50), (255, 255, 255))
            if pg.key.get_pressed()[pg.K_ESCAPE]:
                self.pause_menu()

            if self.is_running:
                if self.is_human:
                    self.key_checker()
                self.hero.update()

                if self.animation_counter % 10 == 0:
                    self.score += 1

                self.environment.update()
                self.animation_counter += 1
            else:
                self.waiter_counter += 1
                self.graphics.draw_wasted_screen()

                if pg.key.get_pressed()[pg.K_SPACE]:
                    self.back_to_main_menu()

            self.draw_visible_obj()

            if self.animation_counter == FPS:
                self.animation_counter = 0

            pg.display.update()
            self.clock.tick(FPS)
