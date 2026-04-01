from dataclasses import dataclass
from ..models.base import MaterialModel


@dataclass
class Fiber():
    coordinates: tuple  # Coordinates of the fiber
    area: float
    model: MaterialModel
    color: str = "red"


@dataclass
class RectPatch():
    coordI: tuple       # Coordinates of the inferior left corner of the patch
    coordJ: tuple       # Coordinates of the superior right corner of the patch
    divY: int           # Number of divisions along the local Y axis (width)
    divZ: int           # Number of divisions along the local Z axis (depth)
    model: MaterialModel
    color: str = "lightgrey"


@dataclass
class LayerFiber():
    coordI: tuple      # Coordinates of the initial and ending point
    coordJ: tuple
    nFiber: int             # Number of Fibers along the layer
    color: str = "red"
