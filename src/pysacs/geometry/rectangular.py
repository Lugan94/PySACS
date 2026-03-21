class RectangularSection:
    """
    Parameters
    ----------
    width : float
        WIDTH OF THE RC SECTION.
    depth : float
        DEPTH OF THE RC SECTION.
    cover : float
        CLEAR COVER OF THE RC SECTION.
    """
    def __init__(self, width, depth, cover):
        self.B = width
        self.D = depth
        self.cover = cover
    
    def is_rectangular(self):
        return True
