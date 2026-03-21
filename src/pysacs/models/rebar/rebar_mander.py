from functools import cached_property
import numpy as np

class Rebar_Mander:
    def __init__(self, rebar):
        self.rebar = rebar

    @cached_property
    def parameters(self):        
        return (
            self.rebar.Es,
            self.rebar.fye,
            self.rebar.fue,
            self.rebar.esh,
            self.rebar.esu,
            self.rebar.P
        )

    def stress(self, strain):
        # Parameters for clarity
        Es, fye, fue, esh, esu, P = self.parameters
        
        strain = np.asarray(strain)
        
        ey = fye / Es
        
        conditions = [
            strain <= ey,
            (strain > ey) & (strain <= esh),
            (strain > esh) & (strain <= esu),
            strain > esu
            ]
        
        functions = [
            lambda strain: strain*Es,
            lambda strain: fye,
            lambda strain: fue + (fye - fue)*abs((esu-strain)/(esu-esh))**P,
            0
            ]
        
        return np.piecewise(strain, conditions, functions)