from ..section import Section
from dataclasses import dataclass
import numpy as np

@dataclass
class MomentCurvatureResults():
    pass


class MomentCurvatureAnalysis():
    def __init__(self, section: Section, angle: float, axial_load: float = 0.0):
        self.section = section
        self.angle = angle
        self.coords, self.areas, self.models = self.parse_fibers()


    def parse_fibers(self) -> tuple[np.ndarray, np.ndarray, list]:      
        coords, areas, models = self.section.fiber_data
        centered_coords = coords - self.section.centroid

        return centered_coords, areas, models

    
    def rotate_coords(self) -> np.ndarray:
        angle = np.radians(self.angle)
        rotation_matrix = np.array([
            [np.cos(angle), -np.sin(angle)],
            [np.sin(angle), np.cos(angle)]
             ])
        
        return  self.coords @ rotation_matrix


    def strain(self, c, phi):
        max_fiber_depth = np.max(self.coords[:,1])
        strains = phi * (max_fiber_depth - c - self.coords[:,1])

        return strains


    def equilibrium(self, c, phi):
        ...