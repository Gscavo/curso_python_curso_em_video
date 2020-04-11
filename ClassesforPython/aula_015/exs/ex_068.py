from random import randint
from time import sleep
a = ''
b = 'PAR OU ÍMPAR'

print(f'{a:~^20}')
print(f'{b: ^20}')
print(f'{a:~^20}')

g = 0
n = 0

while g == 0:
    x = randint(1, 10)
    num = int(input(f'Escolha um número: '))
    print('.')
    sleep(1)
    print('.')
    sleep(1)
    pi = str(input(f'Você escolhe Par ou Ímpar? '))
    print('.')
    sleep(1)
    print('.')
    sleep(1)
    if (num+x) % 2 == 1:
        if pi in 'Ii':
            print(f'!Parabéns!\nEu joguei o número {x} e você o número {num}\n.\n{x}+{num}={x+num}\n.\nO número {x+num} é Ímpar.')
            n += 1
            print('.')
            sleep(1)
            print('.')
            sleep(1)
        else:
            print(f'!Que pena!\nEu joguei o número {x} e você o número {num}\n.\n{x}+{num}={x + num}\n.\nO número {x + num} é Ímpar, portanto, eu ganhei\nVocê ganhou de mim {n} vezes.')
            break
    if (num+x) % 2 == 0:
        if pi in 'Pp':
            print(f'!Parabéns!\nEu joguei o número {x} e você o número {num}\n.\n{x}+{num}={x + num}\n.\nO número {x + num} é Par.')
            n += 1
            print('.')
            sleep(1)
            print('.')
            sleep(1)
        else:
            print(f'!Que pena!\nEu joguei o número {x} e você o número {num}\n.\n{x}+{num}={x + num}\n.\nO número {x + num} é Par, portanto, eu ganhei\nVocê ganhou de mim {n} vezes.')
            break
