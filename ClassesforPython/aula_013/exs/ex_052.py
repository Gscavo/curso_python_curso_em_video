#Número Primo ou Não:

from time import sleep

#Cores:
branco = '\033[1;30m'
vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
lilas = '\033[1;35m'
ciano = '\033[1;36m'
cinza = '\033[1;37m'
normal = '\033[m'

nome = ('{}{}{}'.format(azul, 'Descobrindo se o número é primo ou não', normal))

print('{:.^75}'.format(nome))

print('')

n = int(input('Digite aqui um número inteiro: '))

x=0

#Algoritimo:
for c in range(1, n):
    if n % c == 0:
        x = (x+1)
    elif n % c > 0:
        x = (x+0)

if x>1:
    print('O número {}{}{} não é PRIMO.'.format(verde, n, normal))
else:
    print('O número {}{}{} é {}PRIMO{}.'.format(amarelo, n, normal, vermelho, normal))
