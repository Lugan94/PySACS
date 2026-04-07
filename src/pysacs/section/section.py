from dataclasses import dataclass, field
from ..fibers import Fiber, Patch, Layer


@dataclass(slots=True)
class Section:
    fibers: list[Fiber] = field(default_factory=list)
    patches: list[Patch] = field(default_factory=list)
    layers: list[Layer] = field(default_factory=list)


    def addFibers(self, new_fibers: list[Fiber]):
        if isinstance(new_fibers, list):
            self.fibers.extend(new_fibers)
        else:
            self.fibers.append(new_fibers)
    

    def addPatches(self, new_patches: list[Patch]):
        if isinstance(new_patches, list):
            self.patches.extend(new_patches)
        else:
            self.patches.append(new_patches)
    

    def addLayers(self, new_layers: list[Layer]):
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