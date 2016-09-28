class DefineTypeUnpauredSpin(object):
    level = 0
    sub_level = ''
    j = 0
    energy_level = 0
    parity = 0

    def __init__(self, nucleons):
        if 1 <= nucleons <= 2:
            self.level = 0
            self.sub_level = '1s'
            self.j = 1./2.
            self.energy_level = 1 # 1 para nivel inferior, 2 para nivel superior
        elif 3 <= nucleons <= 6:
            self.level = 1
            self.sub_level = '1p'
            self.j = 3./2.
            self.energy_level = 1
        elif 7 <= nucleons <= 8:
            self.level = 1
            self.sub_level = '1p'
            self.j = 1./2.
            self.energy_level = 2
        elif 9 <= nucleons <= 14:
            self.level = 2
            self.sub_level = '1d'
            self.j = 5./2.
            self.energy_level = 1
        elif 15 <= nucleons <= 16:
            self.level = 0
            self.sub_level = '2s'
            self.j = 1./2.
            self.energy_level = 1
        elif 17 <= nucleons <= 20:
            self.level = 2
            self.sub_level = '1d'
            self.j = 3./2.
            self.energy_level = 2
        elif 21 <= nucleons <= 28:
            self.level = 3
            self.sub_level = '1f'
            self.j = 7./2.
            self.energy_level = 1
        elif 29 <= nucleons <= 32:
            self.level = 1
            self.sub_level = '2p'
            self.j = 3./2.
            self.energy_level = 1
        elif 33 <= nucleons <= 38:
            self.level = 3
            self.sub_level = '1f'
            self.j = 5./2.
            self.energy_level = 2
        elif 39 <= nucleons <= 40:
            self.level = 1
            self.sub_level = '2p'
            self.j = 1./2.
            self.energy_level = 2
        elif 41 <= nucleons <= 50:
            self.level = 4
            self.sub_level = '1g'
            self.j = 9./2.
            self.energy_level = 1
        elif 51 <= nucleons <= 58:
            self.level = 4
            self.sub_level = '1g'
            self.j = 7./2.
            self.energy_level = 2
        elif 59 <= nucleons <= 64:
            self.level = 2
            self.sub_level = '2d'
            self.j = 5./2.
            self.energy_level = 1
        elif 665 <= nucleons <= 68:
            self.level = 2
            self.sub_level = '2d'
            self.j = 3./2.
            self.energy_level = 2
        elif 69 <= nucleons <= 70:
            self.level = 0
            self.sub_level = '3s'
            self.j = 1./2.
            self.energy_level = 1
        elif 71 <= nucleons <= 82:
            self.level = 5
            self.sub_level = '1h'
            self.j = 11./2.
            self.energy_level = 1
        elif 83 <= nucleons <= 92:
            self.level = 5
            self.sub_level = '1h'
            self.j = 9./2.
            self.energy_level = 2
        elif 93 <= nucleons <= 100:
            self.level = 3
            self.sub_level = '2f'
            self.j = 7./2.
            self.energy_level = 1
        elif 101 <= nucleons <= 104:
            self.level = 1
            self.sub_level = '3p'
            self.j = 3./2.
            self.energy_level = 1
        elif 105 <= nucleons <= 110:
            self.level = 3
            self.sub_level = '2f'
            self.j = 5./2.
            self.energy_level = 2
        elif 111 <= nucleons <= 112:
            self.level = 1
            self.sub_level = '3p'
            self.j = 1./2.
            self.energy_level = 2
        elif 113 <= nucleons <= 126:
            self.level = 6
            self.sub_level = '1i'
            self.j = 13./2.
            self.energy_level = 1
        elif 127 <= nucleons <= 136:
            self.level = 4
            self.sub_level = '2g'
            self.j = 9./2.
            self.energy_level = 1
        elif 137 <= nucleons <= 142:
            self.level = 2
            self.sub_level = '3d'
            self.j = 5./2.
            self.energy_level = 1
        elif 143 <= nucleons <= 154:
            self.level = 6
            self.sub_level = '1i'
            self.j = 11./2.
            self.energy_level = 2
        elif 155 <= nucleons <= 162:
            self.level = 4
            self.sub_level = '2g'
            self.j = 7./2.
            self.energy_level = 2
        elif 163 <= nucleons <= 164:
            self.level = 0
            self.sub_level = '4s'
            self.j = 1./2.
            self.energy_level = 1
        elif 165 <= nucleons <= 168:
            self.level = 2
            self.sub_level = '3d'
            self.j = 3./2.
            self.energy_level = 2
        elif 169 <= nucleons <= 184:
            self.level = 7
            self.sub_level = '1j'
            self.j = 15./2.
            self.energy_level = 1
        self.parity = (-1)**self.level
