import pygame_menu as pgm

from CollisionLogic import CollisionLogic
from Env import Environment
from Graphics import Graphics
from Hero import Human, Hero, Agent
from config import *
from menu import GameMenu
from prop import Cactus, Bird
from CustomException import SaveNNException, LoadNNException
from Saver import Saver


class GameEngine:
    def __init__(self):
        self.__is_running = False

        self.__animation_counter = 0
        self.__waiter_counter = 0
        self.__score = 0

        self.__clock = None
        self.__width = WIDTH
        self.__height = HEIGHT
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

    def save_process(self):
        try:
            weights = self.__hero.save_weights()
            saver = Saver(self.__hero.file_path)
            saver.save(weights)
        except SaveNNException as e:
            print(f'!!! Error: {e.message}')

    def load_process(self):
        try:
            saver = Saver(self.__hero.file_path)
            json_weights = saver.load()
            self.__hero.load_weights(json_weights)
        except LoadNNException as e:
            print(f'!!! Error: {e}')

    def set_hero(self, mode):
        self.__is_human = not mode
        self.__hero = Human() if mode == HUMAN else Agent()

    def __key_checker(self):
        if isinstance(self.__hero, Human):
            pressed = pg.key.get_pressed()
            key_arr = [pg.K_UP, pg.K_SPACE, pg.K_DOWN, pg.K_LCTRL]
            self.__hero.change_state(pressed, key_arr)

    def __collision_stuff(self):
        col_log = CollisionLogic()

        cur_prop = self.__environment.prop_list[0]

        return col_log.check_collision(self.__hero, cur_prop)

    def __update(self):
        while self.__is_running or self.__waiter_counter <= FPS * 4:
            self.__graphics.draw_background(self.__animation_counter, isinstance(self.__hero, Human))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.__is_running = False
                    self.__waiter_counter = FPS * 4

            if self.__collision_stuff():
                self.__is_running = False

            self.__graphics.draw_text("score:{}".format(self.__score), (980, 50), (255, 255, 255))
            if pg.key.get_pressed()[pg.K_ESCAPE]:
                self.__pause_menu()

            if self.__is_running:
                if self.__is_human:
                    self.__key_checker()

                self.__hero.update()

                if self.__animation_counter % 10 == 0:
                    self.__score += 1

                self.__environment.update()
                self.__animation_counter += 1
            else:
                self.__waiter_counter += 1
                self.__graphics.draw_wasted_screen()

                if pg.key.get_pressed()[pg.K_SPACE]:
                    self.__back_to_main_menu()

            self.__draw_visible_obj()

            if self.__animation_counter == FPS:
                self.__animation_counter = 0

            pg.display.update()
            self.__clock.tick(FPS)
