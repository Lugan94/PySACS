from dataclasses import dataclass
from ..models.base import MaterialModel


@dataclass(slots=True)
class Fiber():
    coordinates: tuple[float, float]  # Coordinates of the fiber
    area: float
    model: MaterialModel
    color: str = "red"

