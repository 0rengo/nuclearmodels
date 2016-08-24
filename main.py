# coding: utf-8
# from lib.nuclide import Nuclide
from lib.reader import Reader
# nuclideo_teste = Nuclideo(description=u'Hidrogênio', z=1, a=1)
# print nuclideo_teste.nuclear_radius
# print nuclideo_teste.description



# reader = Reader('dadosNucleares2.txt')
# reader.read_z(4)

# for i in reader.data:
#     print i.symbol
#     print i.a
#     print i.z
#     print i.name

from lib.nuclide_base import NuclideBase

n = NuclideBase()
print n