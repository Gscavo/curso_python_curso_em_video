#Pesos:

map = 0
mep = 0

for c in range(1,6):
    p = float(input('Digite aqui o peso de alguém: '))
    if c == 1:
        map = p
        mep = p
    else:
        if p > map:
            map = p
        elif p < mep:
            mep = p
print('O maior peso é {:.1f}Kg e o menor peso é {:.1f}Kg.'.format(map, mep))