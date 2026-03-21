import math as m

class rc_section:
    """
    Parameters
    ----------
    section : Geometry object
        WIDTH OF THE RC SECTION.
    long_rebar : LongitudinalRebar object
        DEPTH OF THE RC SECTION.
    trans_rebar : TransverseRebar object
        CLEAR COVER OF THE RC SECTION.
    """
    def __init__(self, concrete, section_geometry, long_rebar, trans_rebar):
        self.concrete = concrete
        self.geometry = section_geometry
        self.long = long_rebar
        self.trans = trans_rebar
    
    def get_mander_confined_concrete_parameters(self):
        # PARAMETERS FOR CLARITY
        # Materials
        fpce = self.concrete.fpce
        fye_trans = self.trans.bar.material.fye                # Yield strength of the transverse reinforcement
        eco = self.concrete.eco
        esu = self.trans.bar.material.esu
        
        # Section geometry
        B = self.geometry.B                             # Section width
        D = self.geometry.D                             # Section depth
        cover = self.geometry.cover
        
        # Transverse rebar
        d_trans_bar = self.trans.bar.diameter           # Transverse rebar diameter
        a_trans_bar = self.trans.bar.area               # Transverse rebar area
        trans_n_width = self.trans.n_width              # Number of transverse bars parallel to the width of the section
        trans_n_depth = self.trans.n_depth              # Number of transverse bars parallel to the depth of the section
        s = self.trans.spacing                          # Spacing of transverse reinforcement
        
        # Longitudinal Rebar
        d_long_bar = self.long.bar.diameter             # Longitudinal rebar diameter
        a_long_bar = self.long.bar.area                 # Longitudinal rebar area
        long_n_width = self.long.n_width                # Number of longitudinal bars along the width of the section
        long_n_depth = self.long.n_depth                # Number of longitudinal bars along the depth of the section
        
        # Calculations
        As = ((long_n_width * 2 + long_n_depth * 2) - 4) * a_long_bar
        b_c = B - 2 * cover - d_trans_bar
        d_c = D - 2 * cover - d_trans_bar
        A_c = b_c * d_c
        p_cc = As / A_c
        A_cc = A_c * (1 - p_cc)
        
        # Ineffectevly confined areas
        n_parab_width = long_n_width - 1
        n_parab_depth = long_n_depth - 1
        wp_width = (B - 2 * cover - 2 * d_trans_bar - long_n_width * d_long_bar) / n_parab_width
        wp_depth = (D - 2 * cover - 2 * d_trans_bar - long_n_depth * d_long_bar) / n_parab_depth
        A_parab_width = wp_width**2 / 6
        A_parab_depth = wp_depth**2 / 6
        sum_A_parab = 2 * n_parab_width * A_parab_width + 2 * n_parab_depth * A_parab_depth
        
        # Effective area of confined concrete
        sp = s - d_trans_bar
        A_e = (b_c*d_c - sum_A_parab) * (1 - sp/(2*b_c)) * (1 - sp/(2*d_c))
        ke = A_e / A_cc
        
        # Effective lateral confining stress
        Ast_width = trans_n_width * a_trans_bar
        Ast_depth = trans_n_depth * a_trans_bar
        p_width = Ast_width / (s*d_c)
        p_depth = Ast_depth / (s*b_c)
        fl_width = p_width * fye_trans
        fl_depth = p_depth * fye_trans
        fpl_width = ke * fl_width
        fpl_depth = ke * fl_depth
        fpl_Razvi = (fpl_width*d_c + fpl_depth*b_c) / (d_c + b_c)
        
        # Calculate fpcc
        fpcc = fpce * (-1.254 + 2.254*m.sqrt(1 + (7.94*fpl_Razvi)/fpce) - 2*(fpl_Razvi/fpce))
        
        # Calculate Ec
        if 25 <= self.concrete.fpce <= 40:
            Ec = 4400*m.sqrt(self.concrete.fpce)
        else:
            Ec = 2700*m.sqrt(self.concrete.fpce)
        
        # Calculate ecc
        ecc = eco*(1 + 5*(fpcc/fpce - 1))
        
        # Calculate E_sec
        E_sec = fpcc / ecc
        
        # Calculate ecu -> Ultimate strain of the confined concrete
        # First hoop fracture (Priestley, 1996)
        ecu = 0.004 + (1.4*(p_width+p_depth)*fye_trans*esu)/fpcc
        
        return {"fpcc": fpcc,
                "ecc": ecc,
                "Ec": Ec,
                "E_sec": E_sec,
                "ecu": ecu
                }
        
    # Test for including more section shapes
    def test(self):
        if self.geometry.is_rectangular():
            print("it's rectangular")
        else:
            raise Error("error")
        
        
        
