#Adivinhar um número de 1 a 10:
from time import sleep
from random import randint
#Cores:
branco = '\033[1;30m'
vermelho = '\033[1;31m'
verde = '\033[;32m'
amarelo = '\033[1;33m'
azul = '\033[;34m'
lilas = '\033[1;35m'
ciano = '\033[1;36m'
cinza = '\033[1;37m'
normal = '\033[m'

inicio = ('{}JOGO DA ADIVINHAÇÃO{}'.format(branco, normal))

print('{:=^76}'.format(inicio))

name = str(input('Olá eu sou o Pensante um programa que foi criado para pensar em números.\nComo você se chama? ')).strip().capitalize()

for t in range(0,2):
    sleep(1.3)

print('É um prazer te conhecer {}!'.format(name))

for t in range(0,2):
    sleep(1.3)

print('Agora vamos iniciar o jogo!')

for t in range(0,2):
    sleep(1.3)

print('Primeiro eu irei pensar em um número de 1 a 10.')

for t in range(0,10):
    print('.')
    sleep(0.7)

#Numero:
num = randint(1,10)

print('Pronto!')

for t in range(0,2):
    sleep(1.3)

print('Agora você tem que tentar descobrir qual número é ele.')

print('')

for t in range(0,2):
    sleep(1.3)

totg = 1
guess = int(input('Digite aqui seu palpite: '))

print('')

#while not right guess:
while guess != num:
    totg += 1
    print('Não foi esse o número que pensei')
    sleep(1.5)
    guess = int(input('Tente outro palpite: '))
    print('')

print('{}Você acertou!{} O número que eu estava pensando era o número {}{}{}.'.format(verde, normal, azul, num, normal))
print('Você deu um total de {} palpites.'.format(totg))

