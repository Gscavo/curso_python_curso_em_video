from datetime import date

print('')
print('')

hoje = date.today()
jooj = ('Categorizador do Campeonato de Natação de {}.'.format(hoje.year))

print('{:=^100}'.format(jooj))

print('')

ano = int(input('Digite aqui o seu ano de nascimento: '))

print('')

age = (hoje.year - ano)

if age <= 9:
    print('Você competirá na categoria MIRIM.')

elif 9 < age <= 14:
    print('Você competirá na categoria INFANTIL.')

elif 14 < age <= 19:
    print('Você competirá na categoria JUNIOR.')

elif 19 < age <=20:
    print('Você competirá na categoria SÊNIOR.')

else:
    print('Você competirá na categoria MASTER.')