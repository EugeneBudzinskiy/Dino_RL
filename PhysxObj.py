from abc import ABC
from Interfaces import IPhysicalObject


class PhysicalObject(ABC, IPhysicalObject):
    def __init__(self):
        self._coord = (0, 0)  # X|Y
        self._vel = (0, 0)    # X|Y
        self._acc = (0, 0)    # X|Y
        self._size = (0, 0)   # W|H

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

    def set_vel(self, x_vel: int, y_vel: int):
        self._vel = (x_vel, y_vel)

    def set_coord(self, x_coord: int, y_coord: int):
        self._coord = (x_coord, y_coord)

    def set_acc(self, x_acc: int, y_acc: int):
        self._acc = (x_acc, y_acc)

    def set_size(self, width: int, height: int):
        self._size = (width, height)

    def update(self):
        c_acc_x = self._acc[0]
        c_acc_y = self._acc[1]

        c_vel_x = self._vel[0]
        c_vel_y = self._vel[1]

        c_coord_x = self._coord[0]
        c_coord_y = self._coord[1]

        c_vel_x += c_acc_x
        c_vel_y += c_acc_y

        c_coord_x += c_vel_x
        c_coord_y += c_vel_y

        if c_coord_y < 0:
            c_vel_y = 0
            c_acc_y = 0
            c_coord_y = 0

        self.set_acc(c_acc_x, c_acc_y)
        self.set_vel(c_vel_x, c_vel_y)
        self.set_coord(c_coord_x, c_coord_y)
