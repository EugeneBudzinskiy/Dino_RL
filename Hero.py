from abc import ABC
from PhysxObj import PhysicalObject


class Hero(ABC, PhysicalObject):
    def __init__(self):
        self._gravity_acc = (0, -10)
        self._jump_vel = (0, 10)

        self._state = 0
        self._action_queue = list()

    def _jump(self):
        self._state = 0
        self.update()

    def _sit(self):
        self._state = 2
        self.update()

    def _fall(self):
        self._state = 1
        self.update()

    def get_state(self):
        return self._state

    def set_state(self, state: int):
        if state > 2:
            self._state = 2
        else:
            self._state = state
