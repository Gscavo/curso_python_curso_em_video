lverm = ('\033[1;31m')
lverde = ('\033[1;32m')
lazul = ('\033[1;34m')
lciano = ('\033[1;36m')
lnorm = ('\033[m')
print('')
print('')
valor = float(input('Digite aqui o valor da casa: '))
sal = float(input('Digite aqui o seu salário: '))
anos = float(input('Em quantos anos você pretende pagar a casa: '))
#Valor do empréstimo
pr = valor/(anos*12)
#Total possivel
tot = sal+(sal*0.3)
if pr > tot:
    print('{}!INFELIZMENTE NÃO FOI POSSÍVEL EFETUAR SEU EMPRÉSTIMO!{}'.format(lverm, lnorm))
    print('O valor mensal da sua parcela seria {}R${:.2f}{},'
          '\nE no seu caso, o valor máx. da parcela poderia ser somente {}R${}{}.'
          .format(lazul, pr, lnorm, lverm, tot, lnorm))
elif pr == tot or pr < tot:
    print('{}!!!SEU EMPRÉSTIMO FOI ACEITO POR NOSSA EMPRESA!!!{}'.format(lverde, lnorm))
    print('O valor mensal do seu empréstimo é {}R${:.2f}{}.'.format(lciano, pr, lnorm))