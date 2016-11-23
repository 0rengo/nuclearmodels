# coding: utf-8

from nuclide_base import NuclideBase
# from desdobramentoOOv1 import SplitLevel
from define_type_unpaured_spin import DefineTypeUnpauredSpin


class Nuclide(NuclideBase):
    level = 0 #energy level
    sub_level = '' #energy sublevel
    j = 0 #split energy sublevel
    energy_level = 0 # 1 to lower level or 2 to higher level
    spin = 0.0
    parity = 0
    magnetic_moment = 0.0
    nucleon_type = '' #(neutron,proton)

    @property
    def neutrons_amount(self):
       return self.a - self.z

    @property
    def energy_fermi(self):
    #pass
    # calcula a energia do Nivel de Fermi
    # constantes
        hbar_c = 197.3269631 # em MeV fm
        massnucleon_c2 # deve ser escolhido entre massaprotonc2 e massaneutronc2, se for respectivamente, próton ou nêutron
        massprotonc2 = 938.272013 # em MeV
        massneutronc2 = 939.565346 # em MeV
        pi = 3.14159265359
        nF # deve ser escolhido entre Z e N, se for respectivamente, próton ou nêutron
        radius0_fm = 1.25 # em fm
    # O calculo
        energyFermi = ((nF*9.0*pi/4.0*A)**(2./3.))*hcortadoc**2/2.0*massanucleonc2*raio0fm**2
    # A altura do poco de potencial (em MeV)
        v0 = energyFermi + 8.0

    @property
    def nuclear_radius(self):
        R0 = 1.2*10**-15
        return self.a**(1./3.)*R0

    @property
    def nucleons(self):
        if self.z%2 == 0 and self.neutrons%2 == 1:
            unpaired_nucleon = DefineTypeUnpauredSpin(self.neutrons)
            return {
                    'nucleon_type': 'neutron',
                    'range_neutron': unpaired_nucleon,
                    'range_proton': None,
                    'result': unpaired_nucleon.parity
                }
        elif self.z%2 == 1 and self.neutrons%2 == 0:
            unpaired_nucleon = DefineTypeUnpauredSpin(self.z)
            return {
                    'nucleon_type': 'proton',
                    'range_neutron': None,
                    'range_proton': unpaired_nucleon,
                    'result': unpaired_nucleon.parity
                }

        elif self.z%2 == 1 and self.neutrons%2 == 1:
            unpaired_nucleon_1 = DefineTypeUnpauredSpin(self.neutrons)
            unpaired_nucleon_2 = DefineTypeUnpauredSpin(self.z)
            return {
                    'nucleon_type': 'proton and neutron',
                    'range_neutron': unpaired_nucleon_1,
                    'range_proton': unpaired_nucleon_2,
                    'result': unpaired_nucleon_1.parity * unpaired_nucleon_2.parity
                }            

    def split_level_energy(self):
        self.define_type_unpaired_spin()
        pass

    def calc_magnetic_moment(self):
        pass

    def calc_magnetic_moment_schmidt(self):
        pass
