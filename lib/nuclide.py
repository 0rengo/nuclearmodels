from nuclide_base import NuclideBase
from desdobramentoOOv1 import SplitLevel

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
            self._define_type_unpaired_spin(self.neutrons)
            nucleon_type = 'neutron'
        elif self.z%2 == 1 and self.neutrons%2 == 0:
            self._define_type_unpaired_spin(self.z)
            nucleon_type = 'proton'
        elif self.z%2 == 1 and self.neutrons%2 == 1:
            self._define_type_unpaired_spin(self.z)
            nucleon_type = 'proton and neutron'


    def _define_type_unpaired_spin(self, nucleons):
        if nucleons in(1,2):
            self.level = 0
            self.sub_level = '1s'
            self.j = 1./2.
            self.energy_level = 1 # 1 para nivel inferior, 2 para nivel superior
            parity = (-1)**self.l ## ????? Calcularemos fora???
        elif nucleons in(3,6):
            self.level = 1
            self.sub_level = '1p'
            self.j = 3./2.
            self.energy_level = 1
        elif nucleons in(7,8):
            self.level = 1
            self.sub_level = '1p'
            self.j = 1./2.
            self.energy_level = 2
        elif nucleons in(9,14):
            self.level = 2
            self.sub_level = '1d'
            self.j = 5./2.
            self.energy_level = 1
        elif nucleons in(15,16):
            self.level = 0
            self.sub_level = '2s'
            self.j = 1./2.
            self.energy_level = 1
        elif nucleons in(17,20):
            self.level = 2
            self.sub_level = '1d'
            self.j = 3./2.
            self.energy_level = 2
        elif nucleons in(21,28):
            self.level = 3
            self.sub_level = '1f'
            self.j = 7./2.
            self.energy_level = 1
        elif nucleons in(29,32):
            self.level = 1
            self.sub_level = '2p'
            self.j = 3./2.
            self.energy_level = 1
        elif nucleons in(33,38):
            self.level = 3
            self.sub_level = '1f'
            self.j = 5./2.
            self.energy_level = 2
        elif nucleons in(39,40):
            self.level = 1
            self.sub_level = '2p'
            self.j = 1./2.
            self.energy_level = 2
        elif nucleons in(41,50):
            self.level = 4
            self.sub_level = '1g'
            self.j = 9./2.
            self.energy_level = 1
        elif nucleons in(51,58):
            self.level = 4
            self.sub_level = '1g'
            self.j = 7./2.
            self.energy_level = 2
        elif nucleons in(59,64):
            self.level = 2
            self.sub_level = '2d'
            self.j = 5./2.
            self.energy_level = 1
        elif nucleons in(65,68):
            self.level = 2
            self.sub_level = '2d'
            self.j = 3./2.
            self.energy_level = 2
        elif nucleons in(69,70):
            self.level = 0
            self.sub_level = '3s'
            self.j = 1./2.
            self.energy_level = 1
        elif nucleons in(71,82):
            self.level = 5
            self.sub_level = '1h'
            self.j = 11./2.
            self.energy_level = 1
        elif nucleons in(83,92):
            self.level = 5
            self.sub_level = '1h'
            self.j = 9./2.
            self.energy_level = 2
        elif nucleons in(93,100):
            self.level = 3
            self.sub_level = '2f'
            self.j = 7./2.
            self.energy_level = 1
        elif nucleons in(101,104):
            self.level = 1
            self.sub_level = '3p'
            self.j = 3./2.
            self.energy_level = 1
        elif nucleons in(105,110):
            self.level = 3
            self.sub_level = '2f'
            self.j = 5./2.
            self.energy_level = 2
        elif nucleons in(111,112):
            self.level = 1
            self.sub_level = '3p'
            self.j = 1./2.
            self.energy_level = 2
        elif nucleons in(113,126):
            self.level = 6
            self.sub_level = '1i'
            self.j = 13./2.
            self.energy_level = 1
        elif nucleons in(127,136):
            self.level = 4
            self.sub_level = '2g'
            self.j = 9./2.
            self.energy_level = 1
        elif nucleons in(137,142):
            self.level = 2
            self.sub_level = '3d'
            self.j = 5./2.
            self.energy_level = 1
        elif nucleons in(143,154):
            self.level = 6
            self.sub_level = '1i'
            self.j = 11./2.
            self.energy_level = 2
        elif nucleons in(155,162):
            self.level = 4
            self.sub_level = '2g'
            self.j = 7./2.
            self.energy_level = 2
        elif nucleons in(163,164):
            self.level = 0
            self.sub_level = '4s'
            self.j = 1./2.
            self.energy_level = 1
        elif nucleons in(165,168):
            self.level = 2
            self.sub_level = '3d'
            self.j = 3./2.
            self.energy_level = 2
        elif nucleons in(169,184):
            self.level = 7
            self.sub_level = '1j'
            self.j = 15./2.
            self.energy_level = 1


    def split_level_energy(self):
        self.define_type_unpaired_spin()
        pass

    def calc_magnetic_moment(self):
        pass

    def calc_magnetic_moment_schmidt(self):
        pass
