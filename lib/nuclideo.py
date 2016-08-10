class Nuclideo(object):
    description = ''
    z = 0 #atomic number
    a = 0 #atomic mass
    level = 0 #energy level
    sub_level = 0 #energy sublevel
    j = 0 #split energy sublevel
    spin = 0.0
    parity = 0
    magnetic_moment = 0.0
    nucleon_type = '' #(neutron,proton)


    def __init__(self, description='', z=0, a=0):
        self.description = description
        self.z = z
        self.a = a
        # self.split_level_energy()

    @property
    def neutrons_amount(self):
       return self.a - self.z

    @property
    def energy_fermi(self):
        pass
    
    @property
    def nuclear_radius(self):
        R0 = 1.2*10**-15
        return self.a**(1./3.)*R0

    def define_type_unpaired_spin(self):
        pass

    def split_level_energy(self):
        self.define_type_unpaired_spin()
        pass

    def calc_magnetic_moment(self):
        pass

    def calc_magnetic_moment_schmidt(self):
        pass