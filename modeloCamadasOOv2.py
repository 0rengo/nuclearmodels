# coding: UTF-8

# Programa que calcula as predições do Modelo de Camadas
# Física Nuclear - Gilberto Orengo (g.orengo@gmail.com)
# Centro Universitário Franciscano - Curso: Física Médica

import os
# from os import system
from sairOOv1 import Sair

## Construcao das funcoes
##------------------------------------------------------------------------------
## funcao "sair": imprime saidas do programas (espontanea ou por erro)
#def sair(texto_saida):
#    print(texto_saida + "\n")
#    os._exit(1) #ou os._exit(0)
#------------------------------------------------------------------------------
# funcao "calculos1": executa calculos de energia de ligacao.
#                     Parametros: no. atomico Z, no. massa A, no. neutrons N
def calculos1(Z,A,N):
    a1 = 15.835 # Dados da fórmula semi-empírica
    a2 = 18.33
    a3 = 0.714
    a4 = 23.2
    a5 = 34.0/2.0
    NFproton = 14.40945*((7.0686*float(Z)/float(A))**(2./3.)) # Nível de Fermi p/prótons
    NFneutron = 14.38962*((7.0686*float(N)/float(A))**(2./3.)) # Nível de Fermi p/nêutrons
    EB=-a1*float(A) + a2*(float(A)**(2./3.))+a3*(float(Z)**2)/(float(A)**(1./3.)) +a4*(float((N-Z))**2)/float(A) - a5*(float(A)**(-3./4.))*((-1.0)**float(N)+(-1.0)**float(Z))
    EBA = abs(EB/float(A))
    print(" Energia de ligação (fórmula semi-empírica): %5.2f MeV" % EB)
    print(" En. de lig/núcleon (fórmula semi-empírica): %5.2f MeV" % EBA)
    print(" Energia do nível de Fermi para os nêutrons: %5.2f MeV" % NFneutron)
    print(" Energia do nível de Fermi para os prótons : %5.2f MeV" % NFproton )
    while True:
        resp = raw_input("\n\n Desejas fazer outro cálculo? (S) ou (N): ")
        if  resp == 's' or resp == 'S':
            entrada()
        elif resp == 'n' or resp == 'N':
            Sair("\n Cálculo realizado ... abandonando o programa ... Obrigado!!")
#            sair("\n Cálculo realizado ... abandonando o programa ... Obrigado!!")
#------------------------------------------------------------------------------
# funcao "entrada": executa calculos iniciais e verifica consistencia
#                   dos dados de entrada
def entrada():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("  |**********************************************************|")
    print("  |                                                          |")
    print("  |          MODELOS NUCLEARES: Modelo de Camadas            |")
    print("  |                   by Gilberto Orengo                     |")
    print("  |                                                          |")
    print("  |     Predições para Spin, Paridade, Momento magnético     |")
    print("  |         [ Energia de ligação e Nível de Fermi ]          |")
    print("  |                                                          |")
    print("  |**********************************************************|" + "\n")
    Z = int(input(" Digite o valor de Z (número  atômico) : "))
    if Z>118:
        print("\n .....Valor inválido de Número Atômico (Z)!!!!!")
        while True:
            seguir = raw_input(" Tecle 'S' para reiniciar ou 'N' para sair: ")
            if  seguir == 's' or seguir == 'S':
                return entrada()
            elif seguir == 'n' or seguir == 'N':
                Sair("\n Ok! Abortando a execução do programa ... Até mais!!")
    A = int(input(" Digite o valor de A (número de massa) : "))
    N=A-Z # numero de neutrons do nuclideo
    if N<0:
        print("\n .....Valor(es) inválido(s) ... provavelmente de Número de Massa (A)!!!!!")
        while True:
            seguir = raw_input(" Tecle 'S' para reiniciar ou 'N' para sair: ")
            if  seguir == 's' or seguir == 'S':
                return entrada()
            elif seguir == 'n' or seguir == 'N':
                Sair("\n Ok! Abortando a execução do programa ... Até mais!!")
    else:
        arq_dadosNucleares2 = open("dadosNucleares2.txt","r")
        for linha in arq_dadosNucleares2:
            dado = linha.split()
            if (int(dado[0])==Z) and (int(dado[1])==A):
                print(" ELEMENTO >>>>>>> %s (%s)" %(dado[2],dado[5]))
                print(" O número de nêutrons do nuclídeo %s-%d : %d" %(dado[2],A,N))
                print(" A unidade de massa atômica do %s-%d : %15.11f u" %(dado[2],A,float(dado[4])))
                print(" A energia de ligação por núcleon do %s : %8.6f MeV/A" %(dado[2],float(dado[3])))
                print("\n " + "*"*16 +  " RESULTADOS " + "*"*16 + "\n")
                calculos1(Z,A,N)
                break
            elif int(dado[0])>Z or int(dado[0])==118 and int(dado[1])!=A:
                print("\n Ops!! ...... Algum valor inválido (de Z ou A)!!!!!")
                while True:
                    seguir = raw_input("\n Tecle 'S' para reiniciar ou 'N' para sair: ")
                    if  seguir == 's' or seguir == 'S':
                        return entrada()
                    elif seguir == 'n' or seguir == 'N':
                        Sair("\n Ok! Abortando a execução do programa ... Até mais!!")
        arq_dadosNucleares2.close()
#------------------------------------------------------------------------------
# roda o arquivo principal, que inicia a execução dos cálculos - neste caso "entrada()"

if __name__ == '__main__':
    entrada()


