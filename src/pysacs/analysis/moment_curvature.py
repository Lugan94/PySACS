from __future__ import annotations
from typing import TYPE_CHECKING
from dataclasses import dataclass
from .base import compute_strains, compute_forces, compute_moment, find_equilibrium
import numpy as np

if TYPE_CHECKING:
    from ..section import Section

@dataclass
class MomentCurvatureResults():
    phi: np.ndarray
    moment: np.ndarray


class MomentCurvatureAnalysis():
    def __init__(self, section: Section):
        self.section = section
        self.coords, self.areas, self.models = self.parse_fibers()


    def parse_fibers(self) -> tuple[np.ndarray, np.ndarray, list]:      
        coords, areas, models = self.section.fiber_data
        centered_coords = coords - self.section.centroid

        return centered_coords, areas, models

    
    def rotate_coords(self, angle: float) -> np.ndarray:
        angle = np.radians(angle)
        rotation_matrix = np.array([
            [np.cos(angle), -np.sin(angle)],
            [np.sin(angle), np.cos(angle)]
             ])
        
        return  self.coords @ rotation_matrix



    
    def run(self, phi_max: float, n_steps: int, axial_load: float = 0, angle: float = 0) -> MomentCurvatureResults:
        
        phi_array = np.linspace(0, phi_max, n_steps)
        phi_array[0] = 1e-6
        z_coords = self.rotate_coords(angle)
        strain_limits = (min(model.strain_limits[0] for model in self.models),
                         max(model.strain_limits[1] for model in self.models))
        moments = []

        for phi in phi_array:
            e_ref = find_equilibrium(phi=phi,
                                     z_coords=z_coords,
                                     areas=self.areas,
                                     models=self.models,
                                     strain_limits=strain_limits,
                                     P_target=axial_load)
            strains = compute_strains(e_ref=e_ref,
                                      phi=phi,
                                      z_coords=z_coords)
            forces = compute_forces(strains=strains,
                                    areas=self.areas,
                                    models=self.models)
            moment = compute_moment(forces=forces,
                                    z_coords=z_coords)
            moments.append(moment)
            
        return MomentCurvatureResults(phi=phi_array, moment=np.array(moments))