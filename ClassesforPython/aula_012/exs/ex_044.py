#Cores
vermelho = ('\033[1;31m')
amarelo = ('\033[1;33m')
verde = ('\033[1;32m')
normal = ('\033[m')



inicio = 'CALCULADORA DE PREÇOS'
print('{:=^50}'.format(inicio))

price = float(input('Digite aqui o preço do produto: '))
print('Certo! Então o preço desse produto é {}R${:.2f}{}'.format('\033[1;32m', price, '\033[m'))

print('Formas de pagamento:\n'
      '- À Vista no Cheque ;\n'
      '- Dinheiro ;\n'
      '- Cartão de Crédito.')
method = str(input('Digite aqui sua forma de pagamento: ')).upper()

if method == ('CHEQUE'):
      newprice = price - (0.1*price)
      print('Certo, ao pagar à vista no cheque você tem direito a {}10% de desconto{}.'.format(amarelo, normal))
      print('Portanto o preço do seu produto agora é {}R${:.2f}{}'.format(verde, newprice, normal))

elif method == ('DINHEIRO'):
      newprice = price - (0.1 * price)
      print('Certo, ao pagar em dinheiro você tem direito a {}10% de desconto{}.'.format(amarelo, normal))
      print('Portanto o preço do seu produto agora é {}R${:.2f}{}'.format(verde, newprice, normal))

else:
      met = (str(input('Você deseja pagar à vista ou parcelado: ')).upper()).strip

      if met == ('À VISTA') or ('AVISTA') or ('A VISTA') or ('ÀVISTA'):
            newprice = price - (0.05 * price)
            print('Certo, ao pagar à vista no cartão você tem direito a {}5% de desconto{}.'.format(amarelo, normal))
            print('Portanto o preço do seu produto agora é {}R${:.2f}{}'.format(verde, newprice, normal))

      else:
            parc = int(input('Você deseja parcelar em quantas vezes: '))

            if parc == 2:
                  print('O preço do seu produto agora é {}R${:.2f}{}'.format(verde, newprice, normal))
                  print('Este que será em 2 parcelas de {}R${:.2f}{} sem juros.'.format(amarelo, price / 2, normal))
            else:
                  newprice = price + (0.2 * price)
                  print('Certo, ao pagar parceladdo você possui {}20% de juros{}.'.format(amarelo, normal))
                  print('Portanto o preço do seu produto agora é {}R${:.2f}{}'.format(vermelho, newprice, normal))
                  print('Este que será pago em {}{}{} parcelas de {}R${:.2f}{} com 20% de juros.'.format(amarelo, parc, normal, amarelo, price / parc, normal))