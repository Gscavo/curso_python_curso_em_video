'''Fatorial'''

c = int(input('Digite um número para saber sua fatorial: '))
c1 = c
f=1
while c > 0:
    f *= (c)
    c = (c-1)

print('A fatorial de {} é {}.'.format(c1, f))
