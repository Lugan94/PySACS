from dataclasses import dataclass
from ..models.base import MaterialModel


@dataclass
class Fiber():
    coordinates: tuple  # Coordinates of the fiber
    area: float
    model: MaterialModel
    color: str = "red"

