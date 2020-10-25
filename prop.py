from abc import ABC
from PhysxObj import PhysicalObject
from random import randint


class Prop(PhysicalObject, ABC):
    def __init__(self, height: int, width: int):
        PhysicalObject.__init__(self)
        self._prop_vel = 5
        self._vel = (self._prop_vel, 0)
        self._spawn_height = 0
        self._size = (height, width)
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

    def spawn(self, x: int, y: int):
        self.set_coord(x, y)
        self.is_spawned = True

    def move(self):
        if self.is_spawned:
            self.update()


class Bird(Prop):
    spawnheight = (0, 50)

    def __init__(self, height: int, width: int):
        Prop.__init__(self, height, width)
        self.spawn_height = Bird.spawnheight[randint(0, 1)]


class Cactus(Prop):
    def __init__(self, height: int, width: int):
        Prop.__init__(self, height, width)
        self.spawn_height = 0
