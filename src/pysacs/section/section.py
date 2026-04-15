from dataclasses import dataclass, field
from functools import cached_property
import numpy as np
from ..fibers import Fiber, Patch, Layer


@dataclass
class Section:
    fibers: list[Fiber] = field(default_factory=list)
    patches: list[Patch] = field(default_factory=list)
    layers: list[Layer] = field(default_factory=list)


    def addFibers(self, new_fibers: list[Fiber]):
        self.__dict__.pop("fiber_data", None)
        if isinstance(new_fibers, list):
            self.fibers.extend(new_fibers)
        else:
            self.fibers.append(new_fibers)
    

    def addPatches(self, new_patches: list[Patch]):
        self.__dict__.pop("fiber_data", None)
        if isinstance(new_patches, list):
            self.patches.extend(new_patches)
        else:
            self.patches.append(new_patches)
    

    def addLayers(self, new_layers: list[Layer]):
        self.__dict__.pop("fiber_data", None)
        if isinstance(new_layers, list):
            self.layers.extend(new_layers)
        else:
            self.layers.append(new_layers)


    def mesh(self) -> list[Fiber]:
        
        all_fibers = list(self.fibers)

        for patch in self.patches:
            all_fibers.extend(patch.to_fibers())
        
        for layer in self.layers:
            all_fibers.extend(layer.to_fibers())
        
        return all_fibers
    

    @cached_property
    def fiber_data(self) -> tuple[np.ndarray, np.ndarray, list]:
        fibers = self.mesh()
        coords = np.array([fiber.coordinates for fiber in fibers])
        areas =  np.array([fiber.area for fiber in fibers])
        models = [fiber.model for fiber in fibers]
        return coords, areas, models
    
    @property
    def centroid(self):
        coords, areas, _ = self.fiber_data
        return np.average(coords, axis=0, weights=areas)
    
    @property
    def area(self):
        _, areas, _ = self.fiber_data
        return np.sum(areas)