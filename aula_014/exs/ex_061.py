''' Progressão aritimética com 'While' '''
''' 10 1ºs valores da P.A.: '''

i = int(input('Digite aqui o valor inicial da P.A.: '))
r = int(input('Digite aqui a raiz da P.A.: '))
c = i+(r*10)
#Algoritmo:
while i < c:
    i += r
    j = print(i, end=' -> ')
print('END')
