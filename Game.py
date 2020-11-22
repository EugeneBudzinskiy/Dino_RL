import pygame_menu as pgm
import numpy as np

from CollisionLogic import CollisionLogic
from Env import Environment
from Graphics import Graphics
from Hero import Human, Hero, Agent
from config import *
from menu import GameMenu
from prop import Cactus, Bird


class GameEngine:
    def __init__(self):
        self.__is_running = False
        self.__is_alive = False

        self.__animation_counter = 0
        self.__waiter_counter = 0
        self.__score = 0
        self.__action_queue = []

        self.__width = WIDTH
        self.__height = HEIGHT

        self.__clock = None
        self.__hero = None
        self.__is_human = None

        self.__visible_obj = []
        self.screen = pg.display.set_mode((self.__width, self.__height))

        self.__environment = None
        self.__graphics = Graphics(self.screen)

        pg.init()

    def __create_level(self):
        self.__environment.spawn_prop(FIRST_SPAWN_DISTANCE)
        for props in range(0, NUMBER_OF_EXISTING_PROP):
            self.__environment.spawn_prop()

    def __continue_game(self):
        self.__update()

    def __back_to_main_menu(self):
        menu = GameMenu(GameEngine())
        menu.start_menu(not self.__is_human)

    def __pause_menu(self):
        menu = pgm.Menu(300, 400, 'Pause', theme=pgm.themes.THEME_DARK)
        menu.add_button('Continue', self.__continue_game)
        menu.add_button('End Game', self.__back_to_main_menu)
        menu.add_button('Exit', pgm.events.EXIT)
        menu.mainloop(self.screen)

    def __draw_visible_obj(self):
        self.__visible_obj = []
        self.__visible_obj.append(self.__hero)

        for prop in self.__environment.prop_list:
            if prop.coord[0] < self.__width - prop.size[0]:
                self.__visible_obj.append(prop)

        for obj in self.__visible_obj:
            if isinstance(self.__hero, Agent):
                self.__graphics.draw_obj_without_image(obj)
            elif isinstance(obj, Hero):
                self.__graphics.draw_obj(obj, (self.__animation_counter // 5) % 6)
            elif isinstance(obj, Cactus):
                if not obj.is_visible:
                    obj.make_visible()
                self.__graphics.draw_obj(obj, 0)
            elif isinstance(obj, Bird):
                if not obj.is_visible:
                    obj.make_visible()
                self.__graphics.draw_obj(obj, (self.__animation_counter // 12) % 2)

    def setup(self):
        self.__is_running = True
        self.__waiter_counter = 0
        self.__animation_counter = 0

        self.__environment = Environment()
        self.__create_level()
        self.__clock = pg.time.Clock()

        self.__update()

    def set_hero(self, mode):
        self.__is_alive = True
        self.__is_human = not mode
        self.__hero = Human() if mode == HUMAN else Agent()

    def __collision_stuff(self):
        collision_logic = CollisionLogic()
        current_prop = self.__environment.prop_list[0]

        if collision_logic.check_collision(self.__hero, current_prop):
            self.__is_alive = False

    def __animation_counter_stuff(self):
        self.__animation_counter = (self.__animation_counter + 1) % FPS
        if self.__animation_counter % 10 == 0:
            self.__score += 1

    def __waiter_counter_stuff(self):
        self.__waiter_counter += 1
        if self.__waiter_counter >= FPS * 4:
            self.__waiter_counter = 0
            self.__back_to_main_menu()

    def __key_checker(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                if not self.__is_alive:
                    self.__back_to_main_menu()

                elif 'jump' not in self.__action_queue:
                    self.__action_queue.append('jump')

            elif event.key == pg.K_LCTRL:
                if 'sit' not in self.__action_queue:
                    self.__action_queue.append('sit')

            elif event.key == pg.K_ESCAPE:
                self.__pause_menu()

        elif event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                if 'jump' in self.__action_queue:
                    self.__action_queue.remove('jump')

            elif event.key == pg.K_LCTRL:
                if 'sit' in self.__action_queue:
                    self.__action_queue.remove('sit')

    def __get_admire_state(self):
        print(self.__action_queue)
        if len(self.__action_queue) == 0:
            return 'nothing'
        else:
            return self.__action_queue[0]

    def __update(self):
        while self.__is_running:
            self.__clock.tick(FPS)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.__is_running = False

                elif event.type == pg.KEYDOWN or event.type == pg.KEYUP:
                    self.__key_checker(event)

            if self.__is_alive:
                if self.__is_human:
                    admire_state = self.__get_admire_state()
                else:
                    state_list = ['nothing', 'jump', 'sit']
                    random_index = np.random.randint(len(state_list))
                    admire_state = state_list[random_index]

                self.__collision_stuff()
                self.__hero.change_state(admire_state)
                self.__hero.update()

                self.__environment.update()
                self.__animation_counter_stuff()

                self.__graphics.draw_background(self.__animation_counter, isinstance(self.__hero, Human))
                self.__graphics.draw_text("score:{}".format(self.__score), (980, 50), (255, 255, 255))
                self.__draw_visible_obj()

            else:
                self.__graphics.draw_wasted_screen()
                self.__waiter_counter_stuff()

            # pg.display.update()
