from dataclasses import dataclass
from abc import ABC
from ..models.base import MaterialModel

class Layer(ABC):
    ...


@dataclass
class LayerFiber(Layer):
    coordI: tuple       # Coordinates of the first element
    coordJ: tuple       # Coordinates of the last element
    nFiber: int         # Number of Fibers along the layer
    area: float         # Area of the Fibers along the layer
    model: MaterialModel
    color: str = "red"