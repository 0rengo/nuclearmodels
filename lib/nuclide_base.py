import abc

class NuclideBase(object):
    name = ''
    z = 0 #atomic number
    a = 0 #atomic mass

    # @abc.abstractmethod
    def __init__(self, name=None, z=0, a=0):
        self.name = name
        self.z = z
        self.a = a

    # class Meta:
    #     abstract = True