import numpy as np
from ..fibers import Fiber, Patch, Layer
from ..section import Section



def _meshpatch(patches: list[Patch]) -> list[Fiber]:
    for patch in patches:
        ...


    return meshed_patches


def _meshlayer(patches: list[Layer]) -> list[Fiber]:



    return meshed_layers




def mesh(section: Section) -> list[Fiber]:
    meshed_patches = _meshpatch(section.patches)
    meshed_layers = _meshlayer(section.layers)
    meshed_fibers = section.fibers + meshed_patches + meshed_layers

    return meshed_fibers