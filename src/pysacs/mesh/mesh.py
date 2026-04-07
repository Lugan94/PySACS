import numpy as np
from ..fibers import Fiber, Patch, Layer
from ..section import Section


def mesh(section: Section) -> list[Fiber]:
    
    all_fibers = list(section.fibers)

    for patch in section.patches:
        all_fibers.extend(patch.to_fibers())
    
    for layer in section.layers:
        all_fibers.extend(layer.to_fibers())
    

    return all_fibers

