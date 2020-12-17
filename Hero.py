from abc import ABC

from PhysxObj import PhysicalObject
from image import Image
from config import DINO_SIT_IMAGE, DINO_IMAGE
from config import HERO_SIZE, HERO_SIT_SIZE
from config import HERO_JUMP_VEL
from config import GRAVITY_ACC, MAX_GRAVITY_ACC


class Hero(PhysicalObject, ABC):
    texture_pack = []
    t = []
    for image in DINO_SIT_IMAGE:
        t.append(Image(image, (0, 0)))
    texture_pack.append(t)
    t = []
    for image in DINO_IMAGE:
        t.append(Image(image, (0, 0)))
    texture_pack.append(t)

    def __init__(self):
        super().__init__()
        self._gravity_acc = GRAVITY_ACC
        self._max_gravity_acc = MAX_GRAVITY_ACC

        self._jump_vel = HERO_JUMP_VEL

        self.set_size(HERO_SIZE[0], HERO_SIZE[1])
        self.set_acc(0, self._gravity_acc)

        self._state = 'nothing'
        self._admire_state = 'nothing'

        self._animation_delay = 5
        self._animation_frame_count = 6

        self.texture = []
        self.change_textures()

    def _squish(self):
        self.set_size(HERO_SIT_SIZE[0], HERO_SIT_SIZE[1])

    def _un_squish(self):
        self.set_size(HERO_SIZE[0], HERO_SIZE[1])

    def _jump(self):
        self.set_vel(0, self._jump_vel)

    def _fall(self):
        self.set_acc(0, self._gravity_acc)

    def _quick_fall(self):
        self.set_acc(0, self._max_gravity_acc)

    def get_state(self):
        return self._state

    def change_textures(self):
        self.texture = []
        if self._state == 'sit':
            self.texture = self.texture_pack[0]
        else:
            self.texture = self.texture_pack[1]
        for image in self.texture:
            image.change_location(self.coord)

    def update_state(self):
        if self._admire_state == 'nothing':
            if self.coord[1] <= 0:
                if self._state == 'sit':
                    self._un_squish()
                self._state = 'nothing'
                self._fall()

        elif self._admire_state == 'jump':
            if self._state == 'nothing' or self._state == 'sit' and self.coord[1] == 0:
                self._un_squish()
                self._jump()
                self._fall()
                self._state = 'jump'
            elif self.coord[1] <= 0 and self._state == 'jump':
                self._state = 'nothing'

        elif self._admire_state == 'sit':
            if self._state == 'jump':
                self._quick_fall()
                self._state = 'quick-fall'
            elif self._state == 'nothing' or self._state == 'quick-fall' and self.coord[1] >= 0:
                self._squish()
                self._state = 'sit'

        self.change_textures()

    def change_state(self, admire_state='nothing'):
        self._admire_state = admire_state
        self.update_state()
