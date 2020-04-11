#Somátoria de 6 números pares:

from time import sleep

print('{:.^51}'.format('Somátoria de Números Pares'))

n = 0

for c in range (0,6):
    x = int(input('Digite um número: '))
    print('.')
    sleep(0.3)
    print('.')
    sleep(0.3)

    if x % 2 == 0:
        print('\033[1;33m{}\033[m é \033[1;32mPar\033[m.'.format(x))
        n = (n+x)
    else:
        print('\033[1;33m{}\033[m é \033[1;31mImpar\033[m!'.format(x))
for t in range(0,3):
    print('.')
    sleep(1)
print('A soma dos números \033[1;32mPares\033[m que você digitou é {}{}{}.'.format('\033[1;34m', n, '\033[m'))