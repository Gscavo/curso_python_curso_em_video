print('')
print('')
n0 = int(input('Digite aqui 1 número: ').strip())
n1 = int(input('Digite aqui mais um número: ').strip())
n2 = int(input('Digite aqui o último número: ').strip())
print('')
if n0==n1==n2:
    print('Todos os números são iguais')
else:
    if n0==n1:
        if n0>n2:
            print('O maior número é {} e o menor número é {}.'.format(n0, n2))
        else:
            print('O maior número é {} e o menor número é {}.'.format(n2, n0))
    else:
        if n0==n2:
            if n0>n1:
                print('O maior número é {} e o menor é {}.'.format(n0, n1))
            else:
                print('O maior número é {} e o menor número é {}.'.format(n1, n0))
        else:
            if n1==n2:
                if n1>n0:
                    print('O maior número é {} e o menor número é {}.'.format(n1, n0))
                else:
                    print('O maior número é {} e o menor número é {}.'.format(n0, n1))
            else:
                if n0 > n1> n2:
                    print('O maior número é {} e o menor é {}.'.format(n0, n2))
                else:
                    if n0> n2> n1:
                        print('O maior número é {} e o menor é {}.'.format(n0, n1))
                    else:
                        if n1 > n0> n2:
                            print('O maior número é {} e o menor é {}.'.format(n1, n2))
                        else:
                            if n1> n2> n0:
                                print('O maior número é {} e o menor é {}.'.format(n1, n0))
                            else:
                                if n2> n0> n1:
                                    print('O maior número é {} e o menor é {}.'.format(n2, n1))
                                else:
                                    print('O maior número é {} e o menor é {}.'.format(n2, n0))
