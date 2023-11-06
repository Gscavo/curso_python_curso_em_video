#Cor:
vermelho = '\033[1;31m'
amarelo = '\033[1;4;33m'
normal = '\033[m'


print('')
print('')

inicio = 'Formação de Triângulos'
print('{:=^50}'.format(inicio))

a = float(input('Digite aqui o valor da primeira reta (Em cm): '))
b = float(input('Digite aqui o valor da segunda reta: '))
c = float(input('Digite aqui o valor da última reta: '))

print('')

if a > b:
    ab = a-b
else :
    ab = b-a

if ab <= c <= a + b:
    print('É possivel se formar um triângulo com as retas de {}{}{}cm, {}{}{}cm, {}{}{}cm.'.format(vermelho, a, normal, vermelho, b, normal
                                                                                          , vermelho, c, normal))
    if a == b or a == c or b == c:
        print('E esse triângulo é {}Isóceles{}.'.format(amarelo, normal))
    elif a == b == c:
        print('E esse triângulo é {}Equilátero{}.'.format(amarelo, normal))
    else:
        print('E esse triângulo é {}Escaleno{}.'.format(amarelo, normal))
else:
    print('{}Não é possivel formar um triangulo com essas 3 retas!{}'.format(vermelho, normal))