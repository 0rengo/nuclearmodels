class DefineTypeUnpauredSpin(object):
    level = 0
    sub_level = ''
    j = 0
    energy_level = 0
    parity = 0

    def __init__(self, type_nucleons):
        if 1 <= type_nucleons <= 2:
            self.level = 0
            self.sub_level = '1s'
            self.j = 1./2.
            self.energy_level = 1 # 1 para nivel inferior, 2 para nivel superior
        elif 3 <= type_nucleons <= 6:
            self.level = 1
            self.sub_level = '1p'
            self.j = 3./2.
            self.energy_level = 1
        elif 7 <= type_nucleons <= 8:
            self.level = 1
            self.sub_level = '1p'
            self.j = 1./2.
            self.energy_level = 2
        elif 9 <= type_nucleons <= 14:
            self.level = 2
            self.sub_level = '1d'
            self.j = 5./2.
            self.energy_level = 1
        elif 15 <= type_nucleons <= 16:
            self.level = 0
            self.sub_level = '2s'
            self.j = 1./2.
            self.energy_level = 1
        elif 17 <= type_nucleons <= 20:
            self.level = 2
            self.sub_level = '1d'
            self.j = 3./2.
            self.energy_level = 2
        elif 21 <= type_nucleons <= 28:
            self.level = 3
            self.sub_level = '1f'
            self.j = 7./2.
            self.energy_level = 1
        elif 29 <= type_nucleons <= 32:
            self.level = 1
            self.sub_level = '2p'
            self.j = 3./2.
            self.energy_level = 1
        elif 33 <= type_nucleons <= 38:
            self.level = 3
            self.sub_level = '1f'
            self.j = 5./2.
            self.energy_level = 2
        elif 39 <= type_nucleons <= 40:
            self.level = 1
            self.sub_level = '2p'
            self.j = 1./2.
            self.energy_level = 2
        elif 41 <= type_nucleons <= 50:
            self.level = 4
            self.sub_level = '1g'
            self.j = 9./2.
            self.energy_level = 1
        elif 51 <= type_nucleons <= 58:
            self.level = 4
            self.sub_level = '1g'
            self.j = 7./2.
            self.energy_level = 2
        elif 59 <= type_nucleons <= 64:
            self.level = 2
            self.sub_level = '2d'
            self.j = 5./2.
            self.energy_level = 1
        elif 665 <= type_nucleons <= 68:
            self.level = 2
            self.sub_level = '2d'
            self.j = 3./2.
            self.energy_level = 2
        elif 69 <= type_nucleons <= 70:
            self.level = 0
            self.sub_level = '3s'
            self.j = 1./2.
            self.energy_level = 1
        elif 71 <= type_nucleons <= 82:
            self.level = 5
            self.sub_level = '1h'
            self.j = 11./2.
            self.energy_level = 1
        elif 83 <= type_nucleons <= 92:
            self.level = 5
            self.sub_level = '1h'
            self.j = 9./2.
            self.energy_level = 2
        elif 93 <= type_nucleons <= 100:
            self.level = 3
            self.sub_level = '2f'
            self.j = 7./2.
            self.energy_level = 1
        elif 101 <= type_nucleons <= 104:
            self.level = 1
            self.sub_level = '3p'
            self.j = 3./2.
            self.energy_level = 1
        elif 105 <= type_nucleons <= 110:
            self.level = 3
            self.sub_level = '2f'
            self.j = 5./2.
            self.energy_level = 2
        elif 111 <= type_nucleons <= 112:
            self.level = 1
            self.sub_level = '3p'
            self.j = 1./2.
            self.energy_level = 2
        elif 113 <= type_nucleons <= 126:
            self.level = 6
            self.sub_level = '1i'
            self.j = 13./2.
            self.energy_level = 1
        elif 127 <= type_nucleons <= 136:
            self.level = 4
            self.sub_level = '2g'
            self.j = 9./2.
            self.energy_level = 1
        elif 137 <= type_nucleons <= 142:
            self.level = 2
            self.sub_level = '3d'
            self.j = 5./2.
            self.energy_level = 1
        elif 143 <= type_nucleons <= 154:
            self.level = 6
            self.sub_level = '1i'
            self.j = 11./2.
            self.energy_level = 2
        elif 155 <= type_nucleons <= 162:
            self.level = 4
            self.sub_level = '2g'
            self.j = 7./2.
            self.energy_level = 2
        elif 163 <= type_nucleons <= 164:
            self.level = 0
            self.sub_level = '4s'
            self.j = 1./2.
            self.energy_level = 1
        elif 165 <= type_nucleons <= 168:
            self.level = 2
            self.sub_level = '3d'
            self.j = 3./2.
            self.energy_level = 2
        elif 169 <= type_nucleons <= 184:
            self.level = 7
            self.sub_level = '1j'
            self.j = 15./2.
            self.energy_level = 1
        self.parity = (-1)**self.level
