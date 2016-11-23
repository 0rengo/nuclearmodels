# coding: utf-8
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

# from lib.define_type_unpaured_spin import DefineTypeUnpauredSpin

# teste = int(input(" Input value of Z (atomic number) or N (neutron number): "))

# obj = DefineTypeUnpauredSpin(teste)
# print obj.level
# print obj.sub_level
# print obj.j
# print obj.energy_level
# print obj.parity


# nuc = Nuclide(z=int(input(" Input value of Z: ")), a=int(input(" Input value of a: ")))
# print nuc.nucleons

#testar downloader arquivo de dados
# from lib.download_nuclear_data_file import DownloadNuclearDataFile

# dwd = DownloadNuclearDataFile()
# dwd.download_to(path='/home/robertson/GrupoEstudoPython/nuclearmodels/data_files')

from lib.iaea_data import IAEAData
z = int(input(" Input value of Z (atomic number): "))
a = int(input(" Input value of A (mass number)  : "))
data = IAEAData(z, a)
try:
    nuclide = data.get_nuclide_from_file('dados.txt')
    print nuclide.name
    print nuclide.nuclear_radius
    print nuclide.nucleons
except Exception as e:
    print e
