from dataclasses import dataclass
import numpy as np
from .base import MaterialModel


@dataclass(slots=True)
class Hognestad(MaterialModel):
    fpc: float
    Ec: float
    eco: float = 0.002
    ecu: float = 0.004
    ft: float = 0.0

    def stress(self, strain) -> np.ndarray:
        fpc = -self.fpc
        Ec = self.Ec
        eco = -self.eco
        ecu = -self.ecu
        ft = self.ft
        ec = np.asarray(strain)

        et = ft/Ec
        print(et)

        condlist = [
            ec < ecu,
            (ec >= ecu) & (ec < eco),
            (ec >= eco) & (ec < 0.0),
            (ec >= 0.0) & (ec < et),
            ec > et
        ]

        funclist = [
            0.0,
            lambda ec: fpc*(1 - 0.15*(ec-eco)/(ecu-eco)),
            lambda ec: fpc*(2*(ec/eco) - (ec/eco)**2),
            lambda ec: ec*Ec,
            0.0
        ]

        stress = np.piecewise(ec,condlist,funclist)
        return stress
    
@dataclass(slots=True)
class ManderConcrete(MaterialModel):
    fpcc: float
    ecc: float
    Ec: float
    E_sec: float
    ecu: float
    ft: float = 0.0

    def stress(self, strain):
        fpcc = -self.fpcc
        ecc = -self.ecc
        ecu = -self.ecu
        Ec = self.Ec
        ft = self.ft
        ec = np.asarray(strain)

        r = Ec / (Ec - self.E_sec)
        et = ft / Ec

        def mander_curve(ec):
            x = ec / ecc
            return (fpcc * x * r) / (r - 1 + x**r)

        condlist = [
            ec < ecu,
            (ec >= ecu) & (ec < 0.0),
            (ec >= 0.0) & (ec < et),
            ec >= et
        ]

        funclist = [
            0.0,
            mander_curve,
            lambda ec: ec * Ec,
            0.0
        ]

        stress = np.piecewise(ec, condlist, funclist)
        return stress


