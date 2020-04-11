print('')
print('')
v = float(input('Digite a velocidade que o carro estava: '))
if v > 80:
    multa = (7*(v-80))
    print('{:=^55}'.format('!VOCÊ FOI MULTADO!'))
    print('O valor da sua multa é de R${:.2f}'.format(multa))
else:
    print('Você estava dentro do limite de velocidade!')
    print('')
    print('Continue assim!')
    print('E não se esqueça de por cintos de segurança!')