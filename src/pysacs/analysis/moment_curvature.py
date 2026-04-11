from ..section import Section
from dataclasses import dataclass
import numpy as np

@dataclass(slots=True)
class MomentCurvatureResults():
    pass


class MomentCurvatureAnalysis():
    def __init__(self, section: Section):
        self.section = section
        self.fibers = section.mesh()
        self.coords, self.areas  = self.parse_coords()
        self.analysis_coords = self.rotate_coords()


    def parse_coords(self) -> tuple[np.ndarray, np.ndarray]:      
        coords = np.array([fiber.coordinates for fiber in self.fibers])
        areas =  np.array([fiber.area for fiber in self.fibers])
        
        return coords, areas
    

    def rotate_coords(self) -> np.ndarray:
        angle = np.radians(90)
        rotation_matrix = np.array([
            [np.cos(angle), -np.sin(angle)],
            [np.sin(angle), np.cos(angle)]
             ])
        
        return  self.coords @ rotation_matrix


