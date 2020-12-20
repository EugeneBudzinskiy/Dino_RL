from CollisionLogic import CollisionLogic
from Env import Environment
from Graphics import Graphics
from Hero import Hero
from menu import GameMenu
from config import *


class GameEngine:
    def __init__(self):
        self.is_running = False
        self.is_alive = False
        self.is_train = False
        self.is_human = True

        self.__hero = Hero()

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

    @staticmethod
    def off_screen():
        pg.display.iconify()

    def setup(self):
        self.is_running = True
        self.is_alive = True

        self.__action_queue = []
        self.__score = 0

        self.__hero = Hero()
        self.__environment = Environment()

        self.__environment.create_level()
        self.__clock = pg.time.Clock()

    def __key_checker(self, event):
        if not self.is_train:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.menu.pause_menu()

                elif event.key == pg.K_SPACE:
                    if not self.is_alive:
                        self.menu.start_menu()

                    elif 'jump' not in self.__action_queue:
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

    def get_state(self):
        cur_prop = self.__environment.prop_list[0]

        hero_y = self.__hero.coord[1]
        hero_x_size, hero_y_size = self.__hero.size
        hero_r_u_x = hero_x_size
        hero_r_u_y = hero_y + hero_y_size
        hero_vel_y = self.__hero.vel[1]
        hero_acc_y = self.__hero.acc[1]

        prop_x, prop_y = cur_prop.coord
        prop_x_size, prop_y_size = cur_prop.size
        prop_r_u_x = prop_x + prop_x_size
        prop_r_u_y = prop_y + prop_y_size
        prop_vel_x = cur_prop.vel[0]

        hero_y /= self.__height
        hero_r_u_x /= self.__width
        hero_r_u_y /= self.__height
        hero_vel_y /= MAX_VEL
        hero_acc_y /= MAX_ACC

        prop_x /= self.__width
        prop_y /= self.__height
        prop_r_u_x /= self.__width
        prop_r_u_y /= self.__height
        prop_vel_x /= MAX_VEL

        result = [hero_y, hero_r_u_x, hero_r_u_y, hero_vel_y, hero_acc_y,
                  prop_x, prop_y, prop_r_u_x, prop_r_u_y, prop_vel_x]
        return result

    def get_all_info(self):
        next_state = self.get_state()
        reward = 1
        done = not self.is_alive

        return next_state, reward, done

    def render(self):
        self.__clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit(0)
            else:
                self.__key_checker(event)

        if not self.is_alive:
            finished = self.__graphics.draw_wasted_screen()
            if finished:
                self.menu.start_menu()
        else:
            visible_obj = self.__environment.prop_list
            self.__graphics.draw(self.__hero, visible_obj, self.__score, STANDARD_MODE)

        pg.display.update()

    def step(self, action):
        self.__score += 1

        self.__collision_check()

        self.__hero.change_state(action)
        self.__hero.update()
        self.__environment.update()
