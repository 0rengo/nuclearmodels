
# calcula a energia de ligacao (BE) pela formula semi-empirica
# constantes
a1=15.835 , a2=18.33 , a3=0.714 , a4=23.2 ,a5= 34.0/2.0

BE = -a1*A + a2*(A**(2./3.))+a3*(Z**2)/(A**(1./3.)) +a4*((N-Z)**2)/A - a5*(A**(-3./4.))*((-1.0)**N+(-1.0)**Z)
B = -BE/A

# calcula a energia de ligacao (BEe) pela formula de Einstein
# constantes
uc2 = 931.494028 # em MeV
massaproton = 1.00727646677 # em unidades de massa atomica
massaneutron = 1.00866491597
# massanuclideo >> vem do banco de dados

BEe = (Z*massaproton - (A-Z)*massaneutron - massanuclideo)*uc2
Be = -BE/A

# calcula o raio nuclear
#constante
raio0 = 1.25*10**(-15) # 1.25e-15 e em metros

raionuclear = raio0*A**(1/3)

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

# calcula o momento de dipolo magnetico
# precisa do "desdobramento"
# j e l vem do desdobramento

# Calcula o momento magnetico para o proton
# constantes
s = 1/2
muproton=((5.58*(j*(j+1.0) + s*(s+1.0) - l*(l+1.0)) + (j*(j+1.0) - s*(s+1) + l*(l+1.0)))/(2.0*j*(j+1.0)))*j

# Calcula o momento magnetico para o neutron
muneutron=-(3.82*(j*(j+1.0) + s*(s+1.0) - l*(l+1.0)))/(2.0*j*(j+1.0))*j

# Calcula o momento magnetico pela proposta de Shmidt
# constantes
# decide se é para próton ou nêutron para usar o gl e gs
# protons
gl = 1.0
gs = 5.59
# neutrons
gl = 0.0
gs = -3.83

# para a maior energia (energy = 2)
mu=j*gl + ((j)/(2.0*(j+1.0)))*(gl-gs)

# para a menor energia (energy = 1)
mu=j*gl - (1.0/2.0)*(gl-gs)
