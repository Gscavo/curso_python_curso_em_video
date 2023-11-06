from math import pow

#Cores
vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
normal = '\033[m'

print('')
print('')

inicio = 'ÍNDICE DE MASSA CORPOREA (IMC)'
print('{:=^70}'.format(inicio))

altura = float(input('Digite aqui a sua altura em metros: '))
massa = float(input('Digite aqui quanto você pesa, ou seja sua massa, em Kg: '))

print('')

imc =  massa / (altura.__pow__(2))

if imc < 18.5:
    print('{}VOCÊ ESTÁ ABAIXO DO PESO!{}'.format(azul, normal))
    print('Seu IMC é de {}{:.2f}{}.'.format(azul, imc, normal))
    print('Procure um nutricionista para fazer uma dieta'
          ' rica em proteínas!')

elif 18.5 <= imc < 25:
    print('{}PARABENS! VOCÊ ESTÁ NO PESO IDEAL!{}'.format(
        verde, normal))
    print('Seu IMC é de {}{:.2f}{}.'.format(verde, imc, normal))
    print('Continue assim e não esqueça de se exercitar!')

elif 25 <= imc < 30:
    print('{}VOCÊ ESTÁ COM SOBREPESO{}!'.format(amarelo, normal))
    print('Seu IMC é de {}{:.2f}{}.'.format(amarelo, imc, normal))

elif 30 <= imc < 40:
    print('{}VOCÊ ESTÁ OBESO!{}'.format(vermelho, normal))
    print('Seu IMC é de {}{:.2f}{}.'.format(vermelho, imc, normal))
    print('Procure um médico ou um nutricionista!')

elif 40 <= imc:
    print('{}!!!VOCÊ ESTÁ NA ZONA DE OBESIDADE MÓRBIDA!!!{}'.format(vermelho, normal))
    print('Seu IMC é de {}{:.2f}{}.'.format(vermelho, imc, normal))
    print('Procure um médico o mais rápido possivel!')