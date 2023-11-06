from datetime import date

hj = date.today()

#Data do dia em pt-br:

dd = hj.day
mm = hj.month
yyyy = hj.year

if dd < 10:
    dd = int('0{}'.format(hj.day))
else:
    dd = hj.day

if mm < 10:
    mm = int('0{}'.format(hj.month))
else:
    mm = hj.month
print('{}/{}/{}'.format(dd, mm, yyyy))

day = int(input('Digite aqui o dia em que você nasceu: '))
month = int(input('Digite aqui o mês em que você nasceu: '))
year = int(input('Digite aqui o ano em que você nasceu: '))

#Diferença de meses:
difm = mm - month

#Diferença de anos:
dify = (yyyy - year) + float(difm/12)

#Difereça de tempo:
if dify < 18:
    trest = 18 - (dify)
    print('O tempo restante até seu alistamento pro exército é de aprox.:\033[1;34m {:.1f}anos\033[m, '
          'ou seja, mais ou menos \033[1;31m{:.0f} meses\033[m.'.format(trest, trest*12))
elif dify == 18:
    print('\033[1;31m!CHEGOU A SUA HORA DE SE ALISTAR SERVIÇO MILITAR '
          'PARA SERVIR O SEU PAÍS!\033[m')
    print('Aliste-se na junta militar mais próxima de você!')
    print('O \033[1;32mB\033[1;33mr\033[1;34mas\033[1;33mi\033[1;32ml\033[m precisa de você!')
else:
    print('Você já passou da fase de se alistar para o exército!')
    print('Caso não tenha se alistado, aliste-se o mais rápido possível.')