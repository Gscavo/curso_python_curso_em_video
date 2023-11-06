vermelho = '\033[1;4;31m'
verde = '\033[1;4;32m'
azul = '\033[1;4;34m'
normal = '\033[m'
print('')

nums = (input('Digite aqui 2 números: ')).split()

n1 = int(nums[0])
n2 = int(nums[1])

if n1 > n2:
    print('O maior número é {}{}{}.'.format(azul, n1, normal))
elif n2 > n1:
    print('O maior número é {}{}{}.'.format(vermelho, n2, normal))
else:
    print('Os números {}{}{}, {}{}{}, são {}iguais{}.'.format(azul, n1, normal,
          vermelho, n2, normal, verde, normal))