from random import shuffle
print('')
print('')
n1 = (input('Digite aqui o nome dos quatro alunos: ').split(' '))
print('')
shuffle (n1)
print('A ordem de apresentação dos alunos é {}.'.format(', '.join(n1)))

