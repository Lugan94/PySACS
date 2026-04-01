from dataclasses import dataclass
from abc import ABC
from ..models.base import MaterialModel


class Patch(ABC):
    ...


@dataclass
class RectPatch(Patch):
    coordI: tuple       # Coordinates of the inferior left corner of the patch
    coordJ: tuple       # Coordinates of the superior right corner of the patch
    divY: int           # Number of divisions along the local Y axis (width)
    divZ: int           # Number of divisions along the local Z axis (depth)
    model: MaterialModel
    color: str = "lightgrey"