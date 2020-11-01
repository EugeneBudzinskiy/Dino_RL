from abc import ABC
from PhysxObj import PhysicalObject
from config import HERO_SIZE


class Hero(PhysicalObject, ABC):
    def __init__(self):
        super().__init__()
        self._gravity_acc = -1
        self._jump_vel = 10

        self.set_size(HERO_SIZE[0], HERO_SIZE[1])
        self.set_acc(0, self._gravity_acc)

        self._possible_states = ['nothing', 'fall', 'jump', 'sit']

        self._state = self._possible_states[0]
        self._action_queue = list()

    def _squish(self):
        self.set_size(HERO_SIZE[0], 10)

    def _un_squish(self):
        self.set_size(HERO_SIZE[0], HERO_SIZE[1])

    def _fall(self):
        self._state = "fall"
        self.set_acc(0, self._gravity_acc)

    def _jump(self):
        self._state = "jump"
        self.set_vel(0, self._jump_vel)

    def _sit(self):
        self._squish()
        if self._state == "fall":
            self.set_acc(0, self._gravity_acc * 10)
        else:
            self._state = "sit"

    def _nothing(self):
        if self.coord[1] == 0:
            if self._state == "nothing":
                self._un_squish()

            if self._state == "fall":
                self._state = "nothing"

            if self._state == "sit":
                self.delay += 1
                if self.delay == 10:
                    self.delay = 0
                    self._state = "nothing"

    def get_state(self):
        return self._state


class Human(Hero):
    def __init__(self):
        super().__init__()
        self.delay = 0

    def change_state(self, pressed_button, key_list: list):
        if pressed_button[key_list[0]]:
            self._jump()
            self._fall()
        if pressed_button[key_list[1]]:
            self._sit()

        self._nothing()


class Agent(Hero):
    pass
