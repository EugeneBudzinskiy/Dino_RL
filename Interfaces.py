from abc import ABC, abstractmethod


# Here is all interfaces))


class IPhysicalObject(ABC):
    @abstractmethod
    def coord(self):
        pass

    @abstractmethod
    def vel(self):
        pass

    @abstractmethod
    def acc(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def update(self):
        pass


class IProp(ABC):

    @abstractmethod
    def prop_vel(self):
        pass

    @abstractmethod
    def spawn_height(self):
        pass

    @abstractmethod
    def spawn(self, x: int, y: int):
        pass

    @abstractmethod
    def move(self):
        pass
