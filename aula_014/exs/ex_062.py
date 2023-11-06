''' Progressão aritimética com 'While' '''
''' 10 1ºs valores da P.A.: '''
''' + x Valores '''

i = int(input('Digite aqui o valor inicial da P.A.: '))
r = int(input('Digite aqui a raiz da P.A.: '))
x = 10
c = i+(r*x)

#Algoritmo:
while i < c:
    i += r
    print(i, end=' -> ')
print('END')

while x != 0:
    x = int(input('Mais quantos valores dessa P.A. você deseja ver: '))
    c = i+(r*x)
    while i < c:
        i += r
        print(i, end=' -> ')
    print('END')

