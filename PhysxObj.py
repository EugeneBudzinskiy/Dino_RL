from abc import ABC

from Interfaces import IPhysicalObject
from config import GLOBAL_OFFSET, GROUND_LEVEL


class PhysicalObject(IPhysicalObject, ABC):
    def __init__(self):
        self._coord = (0, 0)      # X|Y
        self._vel = (0, 0)        # X|Y
        self._acc = (0, 0)        # X|Y
        self._size = (0, 0)       # W|H
        self._col_size = (0, 0)   # W|H

        self._current_frame = 0
        self._animation_frame = 0
        self._animation_frame_count = 1
        self._animation_delay = 1

    @property
    def animation_frame(self):
        return self._animation_frame

    @property
    def coord(self):
        return self._coord

    @property
    def vel(self):
        return self._vel

    @property
    def acc(self):
        return self._acc

    @property
    def size(self):
        return self._size

    @property
    def col_size(self):
        return self._col_size

    def get_coord_normalized(self, height: int):
        return self._coord[0] + GLOBAL_OFFSET, self._coord[1] + height - GROUND_LEVEL

    def set_vel(self, x_vel: int, y_vel: int):
        self._vel = (x_vel, y_vel)

    def set_coord(self, x_coord: int, y_coord: int):
        self._coord = (x_coord, y_coord)

    def set_acc(self, x_acc: int, y_acc: int):
        self._acc = (x_acc, y_acc)

    def set_size(self, width: int, height: int):
        self._size = (width, height)

    def set_col_size(self, col_width: int, col_height: int):
        self._col_size = (col_width, col_height)

    def update(self):
        self._current_frame = (self._current_frame + 1) % self._animation_delay
        if self._current_frame == 0:
            self._animation_frame = (self._animation_frame + 1) % self._animation_frame_count

        c_acc_x = self._acc[0]
        c_acc_y = self._acc[1]

        c_vel_x = self._vel[0]
        c_vel_y = self._vel[1]

        c_coord_x = self._coord[0]
        c_coord_y = self._coord[1]

        c_vel_x += c_acc_x
        c_vel_y += c_acc_y

        c_coord_x -= c_vel_x
        c_coord_y -= c_vel_y

        if c_coord_y > 0:
            c_vel_y = 0
            c_acc_y = 0
            c_coord_y = 0

        self.set_acc(c_acc_x, c_acc_y)
        self.set_vel(c_vel_x, c_vel_y)
        self.set_coord(c_coord_x, c_coord_y)
