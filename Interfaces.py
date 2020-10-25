from abc import ABC, abstractmethod
# Here is all interfaces))


class IPhysicalObject(ABC):
    @abstractmethod
    def update(self):
        pass
