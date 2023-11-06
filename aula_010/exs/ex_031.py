print('')
print('')
s = float(input('Digite aqui a distância da viagem: '))
print('')
if s<=200:
    print('O preço da sua viagem é de R$0,50 por Km')
    print('Portanto o preço total da sua viagem é de R${:.2f}'.format(s*0.5))
else:
    print('O preço da sua viagem é de R$0,45 por Km')
    print('Portanto o preço total da sua viagem é de R${:.2f}'.format(s*0.45))