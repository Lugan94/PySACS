from dataclasses import dataclass
from abc import ABC, abstractmethod
from ..models.base import MaterialModel
from ..fibers import Fiber
import numpy as np

def db(variable):
    print(f"{variable=}")


class Patch(ABC):
    @abstractmethod
    def to_fibers(self) -> list[Fiber]:
        ...


@dataclass
class RectPatch(Patch):
    coordI: tuple       # Coordinates of the inferior left corner of the patch
    coordJ: tuple       # Coordinates of the superior right corner of the patch
    divY: int           # Number of divisions along the local Y axis (width)
    divZ: int           # Number of divisions along the local Z axis (depth)
    model: MaterialModel
    color: str = "lightgrey"



    def to_fibers(self) -> list[Fiber]:
        width = self.coordJ[0] - self.coordI[0]
        depth = self.coordJ[1] - self.coordI[1]

        fiber_width = width/self.divY
        fiber_depth = depth/self.divZ

        print(f"{width=}")
        print(f"{depth=}")
        print(f"{fiber_width=}")
        db(fiber_depth)

        # fib_y_coords = np.arange(self.coordI[0]+,)

        # db(fib_y_coords)

        meshed_fibers = []
        return meshed_fibers
    
