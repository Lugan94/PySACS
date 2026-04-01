from dataclasses import dataclass
import numpy as np
from .base import MaterialModel

@dataclass
class BilinearEPP(MaterialModel):
    fy: float
    Es: float = 2e6
    esu: float = 0.1171

    def stress(self, strain):
        fy = self.fy
        Es = self.Es
        esu = self.esu
        es = np.asarray(strain)

        ey = fy/Es
        abs_es = np.abs(es)

        condlist = [
            abs_es < ey,
            (abs_es >= ey) & (abs_es <= esu),
            abs_es > esu
        ]

        funclist = [
            lambda es: es*Es,
            lambda es: np.sign(es)*fy,
            0.0
        ]

        stress = np.piecewise(es, condlist, funclist)

        return stress


@dataclass
class BilinearHardening(MaterialModel):
    fy: float
    fu: float
    Es: float = 2e6
    esu: float = 0.1171

    def stress(self, strain):
        fy = self.fy
        Es = self.Es
        esu = self.esu
        fu = self.fu
        es = np.asarray(strain)

        ey = fy/Es
        abs_es = np.abs(es)
        alpha = (fu-fy)/(esu-ey)

        condlist = [
            abs_es < ey,
            (abs_es >= ey) & (abs_es <= esu),
            abs_es > esu
        ]

        funclist = [
            lambda es: es*Es,
            lambda es: np.sign(es) * (fy + alpha*(np.abs(es) - ey)),
            0.0
        ]

        stress = np.piecewise(es, condlist, funclist)

        return stress


@dataclass
class ManderRebar(MaterialModel):
    fy: float
    fu: float
    Es: float = 2e6
    esh: float = 0.0079
    esu: float = 0.1171
    P: float = 3.47

    def stress(self, strain):
        fy = self.fy
        Es = self.Es
        fu = self.fu
        esh = self.esh
        esu = self.esu
        P = self.P
        es = np.asarray(strain)

        ey = fy / Es
        abs_es = np.abs(es)

        condlist = [
            abs_es <= ey,
            (abs_es > ey) & (abs_es <= esh),
            (abs_es > esh) & (abs_es <= esu),
            abs_es > esu
        ]

        funclist = [
            lambda es: es * Es,
            lambda es: np.sign(es) * fy,
            lambda es: np.sign(es) * (fu + (fy - fu) * ((esu - np.abs(es)) / (esu - esh)) ** P),
            0.0
        ]

        stress = np.piecewise(es, condlist, funclist)
        return stress

