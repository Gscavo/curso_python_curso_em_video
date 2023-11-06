''' -Ler 2 valores.
    -Criar um menu:
    [1]-Somar
    [2]-Multiplicar
    [3]-Maior número
    [4]-Add um número
    [5]-Sair do programa'''

c = 0
s = 0
m = 0
v = 0

#Leitura dos 2 Valores
n1 = int(input('Digite aqui um valor: '))
n2 = int(input('Digite aqui um outro valor: '))
#Menu:
print('----Menu----')
print('')
print('''[1]-Somar
[2]-Multiplicar
[3]-Maior número
[4]-Trocar os Números
[5]-Sair do programa''')
print('')

#Algoritmo de escolha do menu:
while c != 5:
    c = int(input('Qual ação deseja realizar:'))
    print('')
    #[1]:
    if c == 1:
        s = (n1+n2)
        print('A soma entre {} e {} é {}'.format(n1, n2, s))
        print('')
    #[2]:
    elif c == 2:
        m = (n1*n2)
        print('A produto da multiplicação de {} e {} é {}'.format(n1, n2, m))
        print('')
    #[3]:
    elif c == 3:
        if n1 > n2:
            print('O número {} é maior que o número {}.'.format(n1, n2))
            print('')
        elif n1 == n2:
            print('O números digitados são iguais.')
            print('')
        else:
            print('O número {} é maior que o número {}.'.format(n2, n1))
            print('')
    #[4]:
    elif c == 4:
        print('''[1]-Para mudar o primeiro valor.
[2]-Para mudar o segundo valor.''')
        print('')
        while v == 0:
            v = int(input('Qual valor você deseja alterar: '))
            print('')
            if v == 1:
                n1 = int(input('Digite aqui um novo número: '))
                print('')
                print('Pronto! Agora os números são {} e {}.'.format(n1, n2))
            elif v == 2:
                n2 = int(input('Digite aqui um novo número: '))
                print('')
                print('Pronto! Agora os números são {} e {}.'.format(n1, n2))
            else:
                print('Desculpe eu não entendi o valor digitado, digite novamente por favor.')
                print('')
            print()
    elif c == 5:
        print('Até mais então!')
        print('Tenha um ótimo dia!')
    else:
        print('Desculpe eu não entendi o valor digitado, digite novamente por favor.')
        print('')
