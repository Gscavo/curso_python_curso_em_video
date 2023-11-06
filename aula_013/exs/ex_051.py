#Progressão aritimética:

branco = '\033[1;30m'
vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
lilas = '\033[1;35m'
ciano = '\033[1;36m'
cinza = '\033[1;37m'
normal = '\033[m'

print('{}{:.^50}{}'.format(vermelho, 'Progressão aritimética', normal))

i = int(input('Digite aqui o termo inicial da P.A: '))

r = int(input('Digite aqui a {}Razão{} da P.A: '.format(branco, normal)))

for c in range(i, i+(r*10), r):
    print(c , end='->')
print('End')