from dataclasses import dataclass
from abc import ABC, abstractmethod
import numpy as np


class MaterialModel(ABC):
    __slots__ = ()
    @abstractmethod
    def stress(self, strain): ...

    @property
    @abstractmethod
    def strain_limits(self) -> tuple[float, float]: ...


@dataclass(slots=True)
class UserModel(MaterialModel):
    strains: list | np.ndarray
    stresses: list | np.ndarray


    def __post_init__(self):
        self.strains = np.asarray(self.strains)
        self.stresses = np.asarray(self.stresses)

        # Sorting the arrays
        sorted_index = np.argsort(self.strains)
        self.strains = self.strains[sorted_index]
        self.stresses = self.stresses[sorted_index]


    def stress(self, strain) -> np.ndarray:
        return np.interp(strain, xp=self.strains, fp=self.stresses)
    

    @property
    def strain_limits(self) -> tuple[float, float]:
        return (np.min(self.strains), np.max(self.strains))

