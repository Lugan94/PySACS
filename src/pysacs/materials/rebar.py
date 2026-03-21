class Rebar:
    """
    Class Rebar
    
    Represents a rebar steel material
    
    Attributes:
        fy (float): Rebar steel yield stress
    """
        
    def __init__(self, fy, fye = None, fue = None, esh = None, esu = None, Es = None, P = None):
        self.fy = fy
        
        # For México, rebar fy = 420 MPa
        if fye is None:
            self.fye = 450.0
        else:
            self.fye = fye
        
        if fue is None:
            self.fue = 730.0
        else:
            self.fue = fue
            
        if esh is None:
            self.esh = 0.0079
        else:
            self.esh = esh
            
        if esu is None:
            self.esu = 0.1171
        else:
            self.esu = esu
        
        if Es is None:
            self.Es = float(2e5)
        else:
            self.Es = Es
            
        if P is None:
            self.P = 3.47
        else:
            self.P = P