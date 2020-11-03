from abc import ABC
from PhysxObj import PhysicalObject
from config import HERO_SIZE


class Hero(PhysicalObject, ABC):
    def __init__(self):
        super().__init__()
        self._gravity_acc = -1
        self._jump_vel = 15

        self.set_size(HERO_SIZE[0], HERO_SIZE[1])
        self.set_acc(0, self._gravity_acc)

        self._state = 'nothing'
        self._admire_state = 'nothing'

    def _squish(self):
        self.set_size(HERO_SIZE[0] + 10, 10)

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
        if pressed_button[key_list[0]]:
            self._admire_state = 'jump'
        elif pressed_button[key_list[1]]:
            self._admire_state = 'sit'
        else:
            self._admire_state = 'nothing'
        self.update_state()


class Agent(Hero):
    pass
