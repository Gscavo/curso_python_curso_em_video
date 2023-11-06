from time import sleep
tabuada = 'TABUADA'

print(f'''{'':~^20}
\033[1;31m{tabuada: ^20}\033[m
{'':~^20}''')

azul = '\033[34m'
normal = '\033[m'
cor = ''
c = 0
cont = 0
numero = 0
a = ''
b = ''
while c == 0:
    print('')
    numero = int(input('Digite aqui um número que você deseja saber a tabuada: '))
    if numero < 0:
        break
    b = f'\033[1;36mTabuada do {numero}\033[m'
    x = len(b)
    print(f'{a:~^{x}}')
    print(f'{b: ^{x}}')
    print(f'{a:~^{x}}')
    if cont != 0:
        cont = 0
    while cont < 10:
        cont += 1
        if cont % 2 == 1:
            cor = '\033[31m'
        elif cont % 2 == 0:
            cor = '\033[32m'
        print(f'{azul}{numero}{normal}x{azul}{cont}{normal}={cor}{numero*cont}{normal}')
        sleep(0.7)
    print('Para parar digite um número negativo.')

