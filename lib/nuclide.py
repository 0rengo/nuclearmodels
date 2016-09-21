from nuclide_base import NuclideBase
from desdobramentoOOv1 import SplitLevel

class Nuclide(NuclideBase):
    level = 0 #energy level
    sub_level = '' #energy sublevel
    j = 0 #split energy sublevel
    spin = 0.0
    parity = 0
    magnetic_moment = 0.0
    nucleon_type = '' #(neutron,proton)


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

    @property
    def nucleons(self):
        if self.z%2 == 0 and self.neutrons%2 == 1:
            self._define_type_unpaired_spin(self.neutrons)
        elif self.z%2 == 1 and self.neutrons%2 == 0:
            self._define_type_unpaired_spin(self.z)
        elif self.z%2 == 1 and self.neutrons%2 == 1:
            self._define_type_unpaired_spin(self.z)


    def _define_type_unpaired_spin(self, nucleons):
        if nucleons in(1,2):
            l = 0
            self.subnivel = '1s'
            j = 1/2 # spin
            energy = 1 # menor
            parity = (-1)**l
        elif nucleons >=3 and nucleons <=6:
            l = 1
            subnivel = 1p
            j = 3/2 # spin
            energy = 1 # menor
            parity = (-1)**l
        elif nucleons >=7 and nucleons <=8:
            l = 1
            subnivel = 1p
            j = 1/2
            energy = 2  # maior
            parity = (-1)**l
        elif nucleons >=9 and nucleons <=14:
            l = 2
            subnivel = 1d
            j = 5/2 #spin
            energy = 1 #menor
            parity = (-1)**l
        elif nucleons >=15 and nucleons <=16:
            l = 0 # 2s1/2
            subnivel = 1d
            j = 1/2 #spin
            energy = 1 #menor
            parity = (-1)**l
        elif nucleons >=17 and nucleons <=20:
            l = 2
            subnivel = 1d
            j = 3/2 #spin
            energy = 2 #maior
            parity = (-1)**l
        elif nucleons >=21 and nucleons <=28:
            l = 3
            subnivel = 1f
            j = 7/2 #spin
            energy = 1 #menor
            parity = (-1)**l
        elif nucleons >=29 and nucleons <=32:
            l = 1
            subnivel = 2p
            j = 3/2 #spin
            energy = 1 #menor
            parity = (-1)**l
        elif nucleons >=33 and nucleons <=38:
            l = 3
            subnivel = 1f
            j = 5/2 #spin
            energy = 2 #maior
            parity = (-1)**l
        elif nucleons >=39 and nucleons <=40:
            l = 1
            subnivel = 2p
            j = 1/2 #spin
            energy = 2 #maior
            parity = (-1)**l
        elif nucleons >=41 and nucleons <=50:
            l = 4
            subnivel = 1g
            j = 9/2 #spin
            energy = 1 #menor
            parity = (-1)**l
        elif nucleons >=51 and nucleons <=58:
            l = 4
            subnivel = 1g
            j = 7/2 #spin
            energy = 2 #maior
            parity = (-1)**l
        elif nucleons >=59 and nucleons <=64:
            l = 2
            subnivel = 2d
            j = 5/2 #spin
            energy = 1 #menor
            parity = (-1)**l
        elif nucleons >=65 and nucleons <=68:
            l = 2
            subnivel = 2d
            j = 3/2 #spin
            energy = 2 #maior
            parity = (-1)**l
        elif nucleons >=69 and nucleons <=70:
            l = 0
            subnivel = 3s
            j = 1/2 #spin
            energy = 1 #menor
            parity = (-1)**l
        elif nucleons >=71 and nucleons <=82:
            l = 5
            subnivel = 1h
            j = 11/2 #spin
            energy = 1 #menor
            parity = (-1)**l
        elif nucleons >=83 and nucleons <=92:
            l = 5
            subnivel = 1h
            j = 9/2 #spin
            energy = 2 #maior
            parity = (-1)**l
        elif nucleons >=93 and nucleons <=100:
            l = 3
            subnivel = 2f
            j = 7/2 #spin
            energy = 1 #menor
            parity = (-1)**l
        elif nucleons >=101 and nucleons <=104:
            l = 1
            subnivel = 3p
            j = 3/2 #spin
            energy = 1 #menor
            parity = (-1)**l
        elif nucleons >=105 and nucleons <=110:
            l = 3
            subnivel = 2f
            j = 5/2 #spin
            energy = 2 #maior
            parity = (-1)**l
        elif nucleons >=111 and nucleons <=112:
            l = 1
            subnivel = 3p
            j = 1/2 #spin
            energy = 2 #maior
            parity = (-1)**l
        elif nucleons >=113 and nucleons <=126:
            l = 6
            subnivel = 1i
            j = 13/2 #spin
            energy = 1 #menor
            parity = (-1)**l
        elif nucleons >=127 and nucleons <=136:
            l = 4
            subnivel = 2g
            j = 9/2 #spin
            energy = 1 #menor
            parity = (-1)**l
        elif nucleons >=137 and nucleons <=142:
            l = 2
            subnivel = 3d
            j = 5/2 #spin
            energy = 1 #menor
            parity = (-1)**l
        elif nucleons >=143 and nucleons <=154:
            l = 6
            subnivel = 1i
            j = 11/2 #spin
            energy = 2 #maior
            parity = (-1)**l
        elif nucleons >=155 and nucleons <=162:
            l = 4
            subnivel = 2g
            j = 7/2 #spin
            energy = 2 #maior
            parity = (-1)**l
        elif nucleons >=163 and nucleons <=164:
            l = 0
            subnivel = 4s
            j = 1/2 #spin
            energy = 1 #menor
            parity = (-1)**l
        elif nucleons >=165 and nucleons <=168:
            l = 2
            subnivel = 3d
            j = 3/2 #spin
            energy = 2 #maior
            parity = (-1)**l
        elif nucleons >=169 and nucleons <=184:
            l = 7
            subnivel = 1j
            j = 15/2 #spin
            energy = 1 #menor
            parity = (-1)**l


    def split_level_energy(self):
        self.define_type_unpaired_spin()
        pass

    def calc_magnetic_moment(self):
        pass

    def calc_magnetic_moment_schmidt(self):
        pass