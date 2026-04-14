import numpy as np


def compute_strains(c: float, phi: float, coords: np.ndarray) -> np.ndarray:
    return phi * (coords - c)


def compute_forces():
    pass


def axial_residual():
    pass

