import math

class Bar:
    """
    Parameters
    ----------
    size : int
    NOMINAL SIZE OF THE BAR.
    """
    # data dictionary: {size: diameter_in_mm}
    _nominal_size = {
        2.5: 7.9,
        3: 9.5,
        4: 12.7,
        5: 15.9,
        6: 19,
        7: 22.2,
        8: 25.4,
        9: 28.6,
        10: 31.8,
        11: 34.9,
        12: 38.1,
        14: 44.5,
        16: 50.8,
        18: 57.2
        }
    
    def __init__(self, size, material):
        if size not in self._nominal_size:
            raise ValueError(f"Bar size #{size} not in available data.")
        
        self.size = size
        self.material = material
        self.diameter = self._nominal_size[size]
        self.area = (math.pi * self.diameter**2) / 4