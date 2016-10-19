# coding: UTF-8
from nuclide_data import NuclideData

#leitor do arquivo de dados
class Reader(object):
    file = None
    nuclide = None

    def __init__(self, file_name):
        try:
            self.file = open(file_name,"r")
        except Exception as e:
            # print e.message
            raise e

    def read_z_a(self, z, a):
        try:
            for line in self.file:
                item = tuple(line.split())
                if (int(nuclide.z)==z and int(nuclide.a)==a):
                    self.nuclide = NuclideData()
                    self.nuclide.z, self.nuclide.a, self.nuclide.symbol, self.nuclide.be_a, self.nuclide.mass_u, self.nuclide.name = item
                    
            if not self.data:
                raise Exception('Invalid mass number or atomic number!')         
        except Exception as e:
            print e.message
        self.file.close()


    # for line in self.file:
    #             data = line.split()
    #             if (int(dado[0])==z) and (int(dado[1])==A):
    #                 print(" ELEMENTO >>>>>>> %s (%s)" %(dado[2],dado[5]))
    #                 print(" O número de nêutrons do nuclídeo %s-%d : %d" %(dado[2],A,N))
    #                 print(" A unidade de massa atômica do %s-%d : %15.11f u" %(dado[2],A,float(dado[4])))
    #                 print(" A energia de ligação por núcleon do %s : %8.6f MeV/A" %(dado[2],float(dado[3])))
    #                 print("\n " + "*"*16 +  " RESULTADOS " + "*"*16 + "\n")
    #                 calculos1(Z,A,N)
    #                 break
    #             elif int(dado[0])>Z or int(dado[0])==118 and int(dado[1])!=A:
    #                 print("\n Ops!! ...... Algum valor inválido (de Z ou A)!!!!!")
    #                 while True:
    #                     seguir = raw_input("\n Tecle 'S' para reiniciar ou 'N' para sair: ")
    #                     if  seguir == 's' or seguir == 'S':
    #                         return entrada()
    #                     elif seguir == 'n' or seguir == 'N':
    #                         Sair("\n Ok! Abortando a execução do programa ... Até mais!!")