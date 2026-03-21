import numpy as np

class Concrete_Mander:
    def __init__(self, *, fpcc, ecc, Ec, E_sec, ecu):
        self.fpcc = fpcc
        self.ecc = ecc
        self.Ec = Ec
        self.E_sec = E_sec
        self.ecu = ecu
    
    def stress(self, strain):
        strain = np.asarray(strain)
        
        x = strain / self.ecc
        r = self.Ec / (self.Ec - self.E_sec)
        stress = (self.fpcc*x*r) / (r - 1 + x**r)

        # Stress is zero beyond ecu        
        stress = np.where(strain > self.ecu, 0.0, stress)
        
        return stress