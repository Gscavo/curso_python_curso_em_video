print('')
print('')
print('Olá eu sou o programa que calcula médias...')
n1 = float(input('Digite aqui a sua primeira nota: '))
print('')
n2 = float(input('Digite aqui a sua segunda nota: '))
print('')
print('Certo! Sua média é {:.1f}.'.format((n1 + n2)/2))
print('')
if ((n1 + n2)/2) >=6:
    print('!PARABÉNS! Você foi aprovado!')
else:
    print('Não foi dessa vez que você conseguiu atingir a média, estude mais da próxima vez!°¬°')