from abc import ABC
from PhysxObj import PhysicalObject


class Hero(PhysicalObject, ABC):
    def __init__(self):
        super().__init__()
        self._gravity_acc = -1
        self._jump_vel = 10

        self.set_acc(0, self._gravity_acc)

        self._possible_states = ['nothing', 'fall', 'jump', 'sit']

        self._state = self._possible_states[0]
        self._action_queue = list()

    def _fall(self):
        self._state = self._possible_states[1]
        self.set_acc(0, self._gravity_acc)

    def _jump(self):
        self._state = self._possible_states[2]
        self.set_vel(0, self._jump_vel)

    def _sit(self):
        if self._state == self._possible_states[2]:
            self.set_acc(0, self._gravity_acc * 10)
        self._state = self._possible_states[3]

    def get_state(self):
        return self._state


class Human(Hero):
    def __init__(self):
        super().__init__()
        self.set_size(10, 10)

    def change_state(self, pressed_button, key_list: list):
        if pressed_button[key_list[0]]:
            # up
            self._jump()
            self._fall()
        if pressed_button[key_list[1]]:
            # down
            self.set_state("sit")


class Agent(Hero):
    pass
