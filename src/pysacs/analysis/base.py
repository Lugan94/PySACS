from __future__ import annotations
from typing import TYPE_CHECKING
from functools import partial
from typing import cast
import numpy as np
from scipy.optimize import brentq

if TYPE_CHECKING:
    from ..fibers import Fiber
    from ..models.base import MaterialModel


def compute_strains(e_ref: float, phi: float, z_coords: np.ndarray) -> np.ndarray:
    return phi * z_coords + e_ref


def compute_forces(strains: np.ndarray, areas: np.ndarray, models: list[MaterialModel]) -> np.ndarray:
    stress = np.zeros(len(strains))
    for i, strain in enumerate(strains):
        stress[i] = models[i].stress(strain)
    
    forces = stress*areas
    return forces
    

def axial_residual(e_ref: float,
                   phi: float,
                   z_coords: np.ndarray,
                   areas: np.ndarray,
                   models: list[MaterialModel],
                   P_target: float = 0.0
                   ) -> float:
    strains = compute_strains(e_ref, phi, z_coords)
    forces = compute_forces(strains, areas, models)
    return np.sum(forces) - P_target
    

def compute_moment(forces: np.ndarray, z_coords: np.ndarray) -> float:
    return np.sum(forces*z_coords)


def find_equilibrium(phi: float,
                    z_coords: np.ndarray,
                    areas: np.ndarray,
                    models: list[MaterialModel],
                    strain_limit: tuple[float, float],
                    P_target: float = 0.0
                    ) -> float:
    eq = partial(axial_residual, phi=phi, z_coords=z_coords, areas=areas, models=models, P_target=P_target)
    e_ref = brentq(eq, strain_limit[0], strain_limit[1], full_output=False)
    return cast(float, e_ref)