from nuclide_base import NuclideBase

class NuclideData(NuclideBase):
    symbol = None
    be_a = None
    mass_u = None

    def __init__(self, z=0, a=0, symbol=None, be_a=None, mass_u=None, name=''):
        self.symbol = symbol
        self.be_a = be_a
        self.mass_u = mass_u
        super(NuclideData, self).__init__(z=z, a=a, name=name)