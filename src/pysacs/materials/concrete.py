class Concrete:
    """
    Class Concrete
    
    Represents an unconfined concrete material
    
    Attributes:
        fc (float): Concrete expected strength
    """
        
    def __init__(self, fpc, eco = None, fpce = None):
        self.fpc = fpc
        
        if eco is None:
            self.eco = 0.002
        else:
            self.eco = eco
        
        if fpce is None:
            self.fpce = 1.3*fpc
        else:
            self.fpce = fpce