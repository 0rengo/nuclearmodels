# coding: utf-8
# from lib.nuclide import Nuclide
# from lib.reader import Reader
# nuclideo_teste = Nuclideo(description=u'Hidrogênio', z=1, a=1)
# print nuclideo_teste.nuclear_radius
# print nuclideo_teste.description


# try:
#     reader = Reader('dadosNucleares2asdfasdf.txt')
#     reader.read_z(120)

#     for i in reader.data:
#         print i.symbol
#         print i.a
#         print i.z
#         print i.name
# except Exception, e:
#     print 'File not found'


# from lib.nuclide_base import NuclideBase

# n = NuclideBase()
# print n

from lib.define_type_unpaured_spin import DefineTypeUnpauredSpin

teste = int(input(" Input value of Z (atomic number) or N (neutron number): "))

obj = DefineTypeUnpauredSpin(teste)
print obj.level
print obj.sub_level
print obj.j
print obj.energy_level
print obj.parity
