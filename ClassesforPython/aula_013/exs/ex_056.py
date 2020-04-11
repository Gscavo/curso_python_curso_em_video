#Nome Idade e Sexo
from time import sleep

#variaveis:
tage = 0
oldman = 0
m = 0
oldname = str()

#Algoritmo:
for c in range(0,4):
    name = str(input('Digite aqui o nome de uma pessoa: '))
    idade = int(input('Digite aqui a idade da pessoa: '))
    print('''[1] - Homem
[2] - Mulher''')
    sexo = int(input('Digite aqui o sexo dessa pessoa: '))
    for y in range(0,3):
        print('.')
        sleep(0.6)
#Total idades;
    tage = (tage+idade)
#Homem + velho:
    if sexo == 1:
        if idade > oldman:
            oldman = idade
            oldname = name
#Mulher com - 20 anos
    if sexo == 2:
        if idade < 20:
            m = (m+1)
#tique-taque:
for t in range (0, 10):
    print('.')
    sleep(0.8)

#Média das idades:
med = float(tage)/4

print('A média das idades do grupo é {} anos,\nO homem mais velho é o {} com {} anos\nE o número de mulheres com menos de 20 anos é de {}.'
      .format(med, oldname, oldman, m))
