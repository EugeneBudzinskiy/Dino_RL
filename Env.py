from random import randint

from config import *
from prop import Bird, Cactus


class Environment:
    def __init__(self):
        self.__prop_list = list()

    @property
    def prop_list(self):
        return self.__prop_list

    def create_level(self):
        self.__spawn_prop(FIRST_SPAWN_DISTANCE)
        for props in range(0, NUMBER_OF_EXISTING_PROP):
            self.__spawn_prop()

    def __spawn_prop(self, x=0):
        type_prop = randint(1, BIRD_SPAWN_CHANCE)

        if type_prop == BIRD_SPAWN_CHANCE:
            instance_prop = Bird(BIRD_SIZE[0], BIRD_SIZE[1])
        else:
            type_cactus = randint(0, len(CACTUS_SIZE)-1)
            instance_prop = Cactus(CACTUS_SIZE[type_cactus][0], CACTUS_SIZE[type_cactus][1])

        if len(self.__prop_list) > 0:
            instance_prop.spawn(self.__prop_list[len(self.__prop_list)-1].coord[0] +
                                self.__prop_list[len(self.__prop_list)-1].size[0] +
                                SPAWN_DISTANCE[randint(0, len(SPAWN_DISTANCE) - 1)])
        else:
            instance_prop.spawn(x)

        self.__prop_list.append(instance_prop)

    def __remove_prop(self, current_prop):
        if current_prop.coord[0] < - GLOBAL_OFFSET * 2:
            self.__prop_list.remove(current_prop)
            self.__spawn_prop(self.__prop_list[len(self.__prop_list) - 1])

    def update(self):
        for prop in self.__prop_list:
            prop.update()

        self.__remove_prop(self.__prop_list[0])
