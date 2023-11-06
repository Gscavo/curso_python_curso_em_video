#Programa q só aceita M ou F:

nome = str(input('Digite aqui o nome de alguém: ')).strip().capitalize()
sexo = str(input(('Sexo [M]/[F]: ')).upper()).strip() [0]

while sexo not in 'MF':
    sexo = str(input('Digite novamente seu sexo [M]/[F]: ')).upper().strip() [0]

if sexo == 'F':
    frase = 'uma mulher'
else:
    frase = 'um homem'

print('{} é {}.'.format(nome, frase))