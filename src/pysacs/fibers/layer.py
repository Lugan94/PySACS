from dataclasses import dataclass
from abc import ABC, abstractmethod
from ..models.base import MaterialModel
from ..fibers import Fiber
import numpy as np

from icecream import ic

class Layer(ABC):
    __slots__ = ()

    @abstractmethod
    def to_fibers(self) -> list[Fiber]:
        ...


@dataclass(slots=True)
class LayerFiber(Layer):
    coordI: tuple       # Coordinates of the first element
    coordJ: tuple       # Coordinates of the last element
    nFiber: int         # Number of Fibers along the layer
    area: float         # Area of the Fibers along the layer
    model: MaterialModel
    color: str = "red"


    def to_fibers(self) -> list[Fiber]:
        fiber_coords = np.linspace(self.coordI,
                                   self.coordJ,
                                   self.nFiber)
        
        meshed_layer = [
            Fiber(coordinates=(float(y), float(z)),
                  area=self.area,
                  model=self.model,
                  color=self.color)
            for y, z in fiber_coords
        ]

        return meshed_layer