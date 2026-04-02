from pysacs.models.rebar import BilinearEPP
from pysacs.models.concrete import Hognestad
from pysacs.fibers.patch import RectPatch
from pysacs.section import Section
# from pysacs.mesh import mesh as m

# rebar = BilinearEPP(4200)
# print(type(rebar))

patch = RectPatch(coordI=(0,0),
                    coordJ=(20,20),
                    divY=5,
                    divZ=4,
                    model=Hognestad(fpc=250,
                                    Ec=14000*250**0.5,
                                    ),
                    color="red")

fibras = patch.to_fibers()
print(fibras)

# section = Section()
# section.addPatches(new_patches=[patch])
# mesh = m.mesh(section=section)
# print(mesh)