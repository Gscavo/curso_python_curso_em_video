''' Leitura de vários Números
    Para com o número 999
    -Número de números digitados
    -Soma deles '''
ns = 0
s = 0
n = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        ns += 1
        s += n
print('Você digitou {} números e a soma deles é {}.'.format(ns, s))