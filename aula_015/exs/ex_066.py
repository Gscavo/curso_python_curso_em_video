#Variáveis
soma = 'SOMATÓRIA DE VALORES'
nu = 0
s = 0
c = 0
n = 0

print(f'''{'':=^30}
\033[1m{soma: ^30}\033[m
{'':=^30}''')

print('Digite 999 para parar.')
print('')
while c == 0:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    nu += 1

print(f'Você digitou {nu} números e a soma entre eles é {s}')