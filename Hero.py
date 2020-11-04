from abc import ABC
from PhysxObj import PhysicalObject
from config import HERO_SIZE,DINO_SIT_IMAGE, DINO_IMAGE, HERO_SIT_SIZE
from image import Image


class Hero(PhysicalObject, ABC):
    def __init__(self):
        super().__init__()
        self._gravity_acc = -1
        self._jump_vel = 15

        self.set_size(HERO_SIZE[0], HERO_SIZE[1])
        self.set_acc(0, self._gravity_acc)

        self._state = 'nothing'
        self._admire_state = 'nothing'
        self.texture = []

    def _squish(self):
        self.set_size(HERO_SIT_SIZE[0], HERO_SIT_SIZE[1])

    def _un_squish(self):
        self.set_size(HERO_SIZE[0], HERO_SIZE[1])

    def _jump(self):
        self.set_vel(0, self._jump_vel)

    def _fall(self):
        self.set_acc(0, self._gravity_acc)

    def _quick_fall(self):
        self.set_acc(0, self._gravity_acc * 5)

    def get_state(self):
        return self._state

    def update_state(self):
        if self._admire_state == 'nothing':
            if self.coord[1] >= 0:
                if self._state == 'squish':
                    self._un_squish()
                self._state = 'nothing'
                self._fall()

        elif self._admire_state == 'jump':
            if self._state == 'nothing' or self._state == 'squish':
                self._un_squish()
                self._jump()
                self._fall()
                self._state = 'jump'
            elif self.coord[1] >= 0 and self._state == 'jump':
                self._state = 'nothing'

        elif self._admire_state == 'sit':
            if self._state == 'jump':
                self._quick_fall()
                self._state = 'quick-fall'
            elif self._state == 'nothing' or self._state == 'quick-fall' and self.coord[1] >= 0:
                self._squish()
                self._state = 'squish'


class Human(Hero):
    def __init__(self):
        super().__init__()

    def change_state(self, pressed_button, key_list: list):
        if pressed_button[key_list[0]] or pressed_button[key_list[1]]:
            self._admire_state = 'jump'
            self.texture = []
            for image in DINO_IMAGE:
                self.texture.append(Image(image, self.coord))
        elif pressed_button[key_list[2]] or pressed_button[key_list[3]]:
            self._admire_state = 'sit'
            self.texture = []
            for image in DINO_SIT_IMAGE:
                self.texture.append(Image(image, self.coord))
        else:
            self._admire_state = 'nothing'
            self.texture = []
            for image in DINO_IMAGE:
                self.texture.append(Image(image, self.coord))
        self.update_state()


class Agent(Hero):
    def __init__(self):
        super().__init__()

        self.brain = None
