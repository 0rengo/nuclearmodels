class Nuclideo(object):
    descricao = ''
    z = 0 #numero atomico
    a = 0 #massa atomica
    nivel = 0 #nivel energetico
    sub_nivel = 0 #subnivel energetico
    j = 0 #desdobramento do subnivel
    energia = 0 #energia do nivel
    spin = 0.0 #resultado do desdobramento
    paridade = 0 #resultado do desdobramento
    momento_magnetico = 0.0
    tipo = '' #se neutron ou proton

    def __init__(self, descricao='', z=0, a=0):
        self.descricao = descricao
        self.z = z
        self.a = a
        self.desdobrar()

    @property
    def numero_neutrons(self):
       return self.a - self.z

    def definir_tipo_desdobramento(self):
        pass

    def desdobrar(self):
        self.definir_tipo_desdobramento()
        pass

    def calcular_momento_magnetico(self):
        pass

    def calcular_momento_magnetico_schmidt(self):
        pass
