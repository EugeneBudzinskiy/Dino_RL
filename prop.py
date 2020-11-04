from abc import ABC
from PhysxObj import PhysicalObject
from random import randint
from Interfaces import IProp
from config import BIRD_SPAWN_HEIGHT, BIRD_IMAGE, CACTUS_IMAGE, CACTUS_SIZE
from image import Image


class Prop(PhysicalObject, IProp, ABC):
    def __init__(self, height: int, width: int):
        super().__init__()
        self._prop_vel = 5
        self._spawn_height = 0

        self.is_visible = False
        self.is_spawned = False
        self.texture = None

        self.set_size(width, height)
        self.set_col_size(int(width * .75), int(height * .75))
        self.set_vel(self._prop_vel, 0)

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
        if height >= 0:
            self._spawn_height = 0
        else:
            self._spawn_height = height

    def spawn(self, x: int):
        self.set_coord(x, self._spawn_height)
        self.is_spawned = True


class Bird(Prop):
    def __init__(self, width: int, height: int):
        super().__init__(height, width)
        self.texture = []

        self.spawn_height = BIRD_SPAWN_HEIGHT[randint(0, len(BIRD_SPAWN_HEIGHT)-1)]

    def make_visible(self):
        for image in BIRD_IMAGE:
            self.texture.append(Image(image, self.coord))
        self.is_visible = True


class Cactus(Prop):
    def __init__(self, width: int, height: int):
        super().__init__(height, width)
        self.texture = []

        self.spawn_height = 0

    def make_visible(self):
        self.texture = []
        if self.size[0] == CACTUS_SIZE[0][0]:
            self.texture = [Image(CACTUS_IMAGE[0], self.coord)]
        elif self.size[0] == CACTUS_SIZE[1][0]:
            self.texture = [Image(CACTUS_IMAGE[1], self.coord)]
        self.is_visible = True
