from abc import ABC
from PhysxObj import PhysicalObject


class Hero(PhysicalObject, ABC):
    def __init__(self):
        super().__init__()
        self._gravity_acc = -10
        self._jump_vel = 10

        self._possible_states = ['nothing', 'fall', 'jump', 'sit']

        self._state = self._possible_states[0]
        self._action_queue = list()

    def _fall(self):
        self._state = self._possible_states[1]
        self.set_acc(0, self._gravity_acc)
        self.update()

    def _jump(self):
        self._state = self._possible_states[2]
        self.set_vel(0, self._jump_vel)
        self.update()

    def _sit(self):
        if self._state == self._possible_states[2]:
            self.set_acc(0, self._gravity_acc * 10)
        self._state = self._possible_states[3]
        self.update()

    def get_state(self):
        return self._state

    def set_state(self, state: str):
        if state in self._possible_states:
            self._state = state
            if state == "fall":
                self._fall()
            elif state == "jump":
                self._jump()
            elif state == "sit":
                self._sit()
        else:
            self._state = self._possible_states[0]


class Human(Hero):
    pass


class Agent(Hero):
    pass
