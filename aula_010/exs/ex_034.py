print('')
print('')
print('{:=^100}'.format('CALCULADORA DE AUMENTO SALARIAL'))
print('')
money = float(input('Digite aqui o seu salário: '))
print('')
if money>1250:
    aument = (money + (money*0.1))
    print('O seu salário, com o aumento salarial de 10%, é igual a R${:.2f}'.format(aument))
else:
    aument = (money + (money * 0.15))
    print('O seu salário, com o aumento salarial de 15%, é igual a R${:.2f}'.format(aument))