from reader import Reader
from nuclide import Nuclide

class IAEAData(object):
    z = None
    a = None

    def __init__(self, z, a):
        self.z = z
        self.a = a

    def get_nuclide_from_file(self, file_name):
        try:
            reader = Reader(file_name)
            reader.read_z_a(self.z, self.a)
            nuclide = Nuclide(name=reader.nuclide_data.name, z=int(reader.nuclide_data.z),
                              a=int(reader.nuclide_data.a))
            return nuclide
        except Exception, e:
            raise e
        
