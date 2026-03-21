
class LongitudinalRebar:
    """
    Parameters
    ----------
    bar : object
        BAR OBJECT.
    n_width : int
        NUMBER OF LONGITUDINAL BARS ALONG THE WIDTH OF THE RC SECTION.
    n_depth : int
        NUMBER OF LONGITUDINAL BARS ALONG THE DEPTH OF THE RC SECTION.
    """
    def __init__(self, bar, n_width, n_depth):
        self.bar = bar
        self.n_width = n_width
        self.n_depth = n_depth
    

class TransverseRebar:
    """
    Parameters
    ----------
    bar : object
        BAR OBJECT.
    n_width : int
        NUMBER OF TRANSVERSE BARS PARALLEL TO THE WIDTH OF THE RC SECTION.
    n_depth : int
        NUMBER OF TRANSVERSE BARS PARALLEL TO THE DEPTH OF THE RC SECTION.
    """
    def __init__(self, bar, n_width, n_depth, spacing):
        self.bar = bar
        self.n_width = n_width
        self.n_depth = n_depth
        self.spacing = spacing

