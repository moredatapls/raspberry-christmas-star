from abc import ABCMeta, abstractmethod


class AbstractStar(metaclass=ABCMeta):
    @abstractmethod
    def set_color(self, r: int, g: int, b: int):
        pass
