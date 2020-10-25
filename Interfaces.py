from abc import ABC, abstractmethod


# Here is all interfaces))


class IPhysicalObject(ABC):
    @abstractmethod
    def update(self):
        pass


class IProp(ABC):

    @abstractmethod
    def spawn(self, x: int, y: int):
        pass

    @abstractmethod
    def move(self):
        pass
