# Tabuada com o For
from time import sleep

n = int(input('Digite aqui o número que deseja saber a tabuada: '))

for t in range(0,6):
    print('.')
    #sleep(0.7)

x = ('Tabuada do {}'.format(n))

print('\033[1;32m{:_^50}\033[m'.format(x))

#Cores:
azul = '\033[1;34m'
vermelho = '\033[1;31m'
amarelo = '\033[1;33m'
normal = '\033[m'


for c in range(1, 11):
    tab = ('{0}{1}{2}x{3}{4}{5}={6}{7}{8}'.format(azul, n, normal, vermelho, c, normal, amarelo, n*c, normal))
    print('{:.>38}'.format(tab))
    sleep(1)