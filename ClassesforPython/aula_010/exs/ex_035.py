print('')
print('')
l1 = float(input('Digite aqui a medida de umas da retas: '))
l2 = float(input('Digite aqui a medida da segunda: '))
l3 = float(input('Digite aqui a medida da última: '))
print('')
if l1>=l2:
    if l1-l2 < l3 < l1+l2 :
        print('É possivel se criar um triângulo com essas 3 retas.')
    else:
        print('Não é possivel se criar um triângulo.')
else:
    if l2-l1 < l3 < l1+l2 :
        print('É possivel se criar um triângulo com essas 3 retas.')
    else:
        print('Não é possivel se criar um triângulo.')