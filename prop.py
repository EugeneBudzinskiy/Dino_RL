from abc import ABC
from PhysxObj import PhysicalObject
from random import randint
from Interfaces import IProp


class Prop(PhysicalObject, IProp, ABC):
    def __init__(self, height: int, width: int):
        super(PhysicalObject).__init__()
        self._prop_vel = 5
        self._vel = (self._prop_vel, 0)
        self._spawn_height = 0
        self._size = self.set_size(width, height)
        self.is_spawned = False

    @property
    def prop_vel(self):
        return self._prop_vel

    @prop_vel.setter
    def prop_vel(self, vel: int):
        self._prop_vel = vel

    @property
    def spawn_height(self):
        return self._spawn_height

    @spawn_height.setter
    def spawn_height(self, height):
        if height <= 0:
            self._spawn_height = 0
        else:
            self._spawn_height = height

    def spawn(self, x: int):
        self.set_coord(x, self._spawn_height)
        self.is_spawned = True

    def move(self):
        if self.is_spawned:
            self.update()


class Bird(Prop):
    # Bird
    spawnheight = (0, 50)

    def __init__(self, height: int, width: int):
        super(Prop).__init__(height, width)
        self.spawn_height = Bird.spawnheight[randint(0, 1)]


class Cactus(Prop):
    def __init__(self, height: int, width: int):
        super(Prop).__init__(height, width)
        self.spawn_height = 0
