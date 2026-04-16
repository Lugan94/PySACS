from __future__ import annotations
import numpy as np
from pysacs.models.rebar import BilinearEPP, BilinearHardening, ManderRebar
from pysacs.models.concrete import Hognestad, ManderConcrete
from pysacs.fibers.fiber import Fiber
from pysacs.fibers.patch import RectPatch
from pysacs.fibers.layer import LayerFiber
from pysacs.section import Section
from pysacs.analysis import MomentCurvatureAnalysis
from icecream import ic
import matplotlib.pyplot as plt

hardening = BilinearHardening(4500, 7300)
hognestad = Hognestad(fpc=250, Ec=14000*250**0.5, ecu=0.003)
rebar = BilinearEPP(4200)
mander = ManderConcrete(fpcc=418.6, ecc=0.004881, Ec=252389, E_sec=85443, ecu=0.0212, ft=36)
rebarmander = ManderRebar(4500, 7300)

# fiber = Fiber(coordinates=(10, 10),
#               area=5,
#               model=hardening,
#               color="blue")

patch = RectPatch(coordI=(-25,-35),
                    coordJ=(25,35),
                    divY=10,
                    divZ=14,
                    model=mander,
                    color="gray")

layer_inf = LayerFiber(coordI=(-20,-31),
                   coordJ=(20,-31),
                   nFiber=4,
                   area=2.85,
                   model=rebarmander,
                    color="red")

layer_sup = LayerFiber(coordI=(-20,31),
                   coordJ=(20,31),
                   nFiber=4,
                   area=2.85,
                   model=rebarmander,
                    color="red")

section = Section()

section.addPatches([patch])
section.addLayers([layer_inf, layer_sup])

ic(section.centroid)
ic(section.area)

analysis = MomentCurvatureAnalysis(section=section)
# ic(analysis.coords)
# ic(analysis.areas)
# ic(analysis.models)

resultados = analysis.run(phi_max=0.004, n_steps=100, axial_load=0, angle=0)
ic(resultados)

plt.plot(resultados.phi, resultados.moment)
plt.show()


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
