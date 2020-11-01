from Interfaces import IProp
from random import randint
from config import *
from prop import Bird, Cactus


class Environment:

    def __init__(self):
        self.__prop_list = list()

    def spawn_prop(self, x=0):
        type_prop = randint(1, BIRD_SPAWN_CHANCE)
        instance_prop = None

        if type_prop == BIRD_SPAWN_CHANCE:
            instance_prop = Bird(BIRD_SIZE[0], BIRD_SIZE[1])
        if type_prop != BIRD_SPAWN_CHANCE:
            instance_prop = Cactus(CACTUS_SIZE[0], CACTUS_SIZE[1])
        if len(self.__prop_list):
            instance_prop.spawn(self.__prop_list[len(self.__prop_list)-1].coord[0] +
                                self.__prop_list[len(self.__prop_list)-1].size[0] +
                                SPAWN_DISTANCE[randint(0, len(SPAWN_DISTANCE) - 1)])
        else:
            instance_prop.spawn(x)
        self.__prop_list.append(instance_prop)

    @property
    def prop_list(self):
        return self.__prop_list

    def remove_prop(self):
        for prop in self.__prop_list:
            if prop.coord[0] < - GLOBAL_OFFSET * 2:
                self.__prop_list.remove(prop)

    def update(self):
        for prop in self.__prop_list:
            prop.update()
        self.remove_prop()
        if len(self.__prop_list) < NUMBER_OF_EXISTING_PROP:
            self.spawn_prop(self.__prop_list[len(self.__prop_list) - 1])
