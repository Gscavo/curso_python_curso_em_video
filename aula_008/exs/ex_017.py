from math import hypot
print('')
print('')
ca = float(input('Digite aqui o comprimento do cateto adjacente: '))
print('')
co = float(input('Digite aqui o comprimento do cateto oposto: '))
print('')
print('O valor da hipotenusa desse triângulo será {:.2f}.'.format(hypot(ca, co)))