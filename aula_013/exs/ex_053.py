#Palíndromos:
from time import sleep

x = (str(input('Escreva aqui uma frase: ')).strip()).upper()

#Retirada dos espaços e junção sem espaços dps
y = x.split()
frase = ''.join(y)

#Contagem de letras:
n = int(len(frase))
s = 0
z = 0

#time:
for t in range(0,6):
    print('.')
    sleep(0.5)



#Algoritimo:
for c in range(n-1, 0, -1):
    z = ((n-1)-c)+0
    if  str(frase[z]) == str(frase[c]):
        s = (s+1)
    else:
        s = (s+0)

if s == n-1:
   print('A frase "{}" é um Palíndromo.'.format(x.capitalize()))
else:
   print('A frase "{}" não é um Palíndromo.'.format(x.capitalize()))