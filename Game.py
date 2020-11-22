import pygame_menu as pgm
import numpy as np

from CollisionLogic import CollisionLogic
from Env import Environment
from Graphics import Graphics
from Hero import Hero
from config import *
from menu import GameMenu
from prop import Cactus, Bird


class GameEngine:
    def __init__(self):
        self.is_running = False
        self.is_human = True
        self.is_alive = False

        self.__hero = Hero()

        self.__waiter_counter = 0
        self.__score = 0
        self.__action_queue = []

        self.__width = WIDTH
        self.__height = HEIGHT

        self.__clock = None
        self.__environment = None

        self.screen = pg.display.set_mode((self.__width, self.__height))

        pg.init()

        self.__graphics = Graphics(self.screen)
        self.menu = GameMenu(self, self.screen)

    def setup(self):
        self.is_running = True
        self.is_alive = True

        self.__waiter_counter = 0
        self.__action_queue = []

        self.__hero = Hero()
        self.__environment = Environment()

        self.__environment.create_level()
        self.__clock = pg.time.Clock()

    # def __animation_counter_stuff(self):
    #     self.__animation_counter = (self.__animation_counter + 1) % FPS
    #     if self.__animation_counter % 10 == 0:
    #         self.__score += 1
    #
    # def __waiter_counter_stuff(self):
    #     self.__waiter_counter += 1
    #     if self.__waiter_counter >= FPS * 4:
    #         self.__waiter_counter = 0
    #         self.__back_to_main_menu()
    #
    def __key_checker(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.menu.pause_menu()

            elif event.key == pg.K_SPACE:
                if 'jump' not in self.__action_queue:
                    self.__action_queue.append('jump')

            elif event.key == pg.K_LCTRL:
                if 'sit' not in self.__action_queue:
                    self.__action_queue.append('sit')

        elif event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                if 'jump' in self.__action_queue:
                    self.__action_queue.remove('jump')

            elif event.key == pg.K_LCTRL:
                if 'sit' in self.__action_queue:
                    self.__action_queue.remove('sit')

    def get_action_from_key_check(self):
        if len(self.__action_queue) == 0:
            return 'nothing'
        else:
            return self.__action_queue[0]

    def __collision_check(self):
        collision_logic = CollisionLogic()
        current_prop = self.__environment.prop_list[0]

        if collision_logic.check_collision(self.__hero, current_prop):
            self.is_alive = False

    def render(self):
        self.__clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit(0)
            else:
                self.__key_checker(event)

        visible_obj = self.__environment.prop_list
        self.__graphics.draw(self.__hero, visible_obj, self.__score)
        pg.display.update()

    def step(self, action):
        self.__hero.change_state(action)
        self.__hero.update()
        self.__collision_check()
        self.__environment.update()
