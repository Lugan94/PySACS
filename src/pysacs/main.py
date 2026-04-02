import numpy as np
from pysacs.models.rebar import BilinearEPP
from pysacs.models.concrete import Hognestad
from pysacs.fibers.patch import RectPatch
from pysacs.fibers.layer import LayerFiber
from pysacs.section import Section
# from pysacs.mesh import mesh as m
from icecream import ic

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

layer = LayerFiber(coordI=(0,0),
                   coordJ=(9,9),
                   nFiber=4,
                   area=2.0,
                   model=Hognestad(fpc=250,
                                    Ec=14000*250**0.5,
                                    ),
                    color="red")

fibras2 = layer.to_fibers()
ic(fibras2)
ic(fibras2[0].coordinates[0])



# import tracemalloc
# from pysacs.fibers import Fiber

# # 1. Iniciar el rastreo
# tracemalloc.start()

# # 2. Tomar foto inicial
# snapshot_inicial = tracemalloc.take_snapshot()

# hognestad = Hognestad(fpc=250, Ec=14000*250**0.5)

# # --- AQUÍ CREAS TUS 25,000 FIBRAS ---
# mis_fibras = [Fiber((1,2), 20.0, model=hognestad, color="red") for _ in range(500)]

# # 3. Tomar foto final y comparar
# snapshot_final = tracemalloc.take_snapshot()
# estadisticas = snapshot_final.compare_to(snapshot_inicial, 'lineno')

# print("[ Comparativa de memoria ]")
# for stat in estadisticas[:5]: # Ver los 3 mayores consumidores
#     print(stat)
