from abc import ABC
from PhysxObj import PhysicalObject


class Hero(ABC, PhysicalObject):
    def __init__(self):
        self._gravity_acc = (0, -10)
        self._jump_vel = (0, 10)

        self._state = 0  # 0 = nothing | 1 = fall | 2 = jump | 3 = sit
        self._action_queue = list()

    def _fall(self):
        self._state = 1
        self.set_acc(self._gravity_acc)
        self.update()

    def _jump(self):
        self._state = 2
        self.set_vel(self._jump_vel)
        self.update()

    def _sit(self):
        if self._state == 1:
            self.set_acc(self._gravity_acc * 10)
        self._state = 3
        self.update()

    def get_state(self):
        return self._state

    def set_state(self, state: int):
        if 0 <= state <= 3:
            self._state = state
        else:
            self._state = 0
