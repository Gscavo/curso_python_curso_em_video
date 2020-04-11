print('')
print('')
n1 = float(input('Digite aqui a sua 1ª nota: '))
n2 = float(input('Digite aqui a sua 2ª nota: '))
print('')
media = (n1+n2)/2
if media < 5:
    print('\033[1;4;31m!REPROVADO!\033[m')
    print('Sua média desse bimestre foi de \033[1;31m{:.1f}\033[m.'.format(media))
    print('\033[1;30mEstude mais no próximo bimestre\033[m')
elif 5<=media<6:
    print('\033[1;4;33m!RECUPERAÇÃO!\033[m')
    print('Você quase atingiu a média '
          'desse bimestre, sendo que sua média '
          'foi de \033[1;33m{:.1f}\033[m.'.format(media))
    print('\033[1;30mEstude mais da próxima vez!\033[m')
else:
    print('\033[1;4;32m!APROVADO!\033[m')
    print('Você alcançou a média!')
    print('Sua média foi \033[1;32m{:.1f}\033[m.'.format(media))