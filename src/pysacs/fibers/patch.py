from dataclasses import dataclass
from abc import ABC, abstractmethod
from ..models.base import MaterialModel
from ..fibers import Fiber
import numpy as np

from icecream import ic


class Patch(ABC):
    __slots__ = ()

    @abstractmethod
    def to_fibers(self) -> list[Fiber]:
        ...


@dataclass(slots=True)
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

        fib_y_coords = np.linspace(self.coordI[0] + fiber_width/2,
                                   self.coordJ[0] - fiber_width/2, 
                                   self.divY)
        fib_z_coords = np.linspace(self.coordI[1] + fiber_depth/2,
                                   self.coordJ[1] - fiber_depth/2,
                                   self.divZ)

        fib_y_coords, fib_z_coords = np.meshgrid(fib_y_coords, fib_z_coords)

        fiber_area = fiber_width * fiber_depth
        
        y_coords = fib_y_coords.ravel().tolist()
        z_coords = fib_z_coords.ravel().tolist()

        meshed_fibers = [
            Fiber(
                coordinates=(y, z),  # Aquí y, z ya son floats nativos
                area=fiber_area,
                model=self.model,
                color=self.color
            )
            for y, z in zip(y_coords, z_coords)
        ]
        
        return meshed_fibers
    
