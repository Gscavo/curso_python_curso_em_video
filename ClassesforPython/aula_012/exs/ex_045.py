from random import choice, shuffle
from time import sleep
print('{:.^30}'.format('JOKENPÔ'))

#lista de jogadas:
pe = ('PEDRA')
pa = ('PAPEL')
te = ('TESOURA')
d = 'S'
print('Vamos jogar Jokenpô?')

while d not in 'N':
    list = (pe, pa, te)
    ppt = choice(list)


    print('''[1]-PEDRA
[2]-PAPEL
[3]-TESOURA''')


    ch = int(input('Escolha sua jogada: '))
    for c in range(0,4):
        print('.')
        sleep(0.5)

    if ch == 1:
        if ppt == pe:
            print('Houve um empate! Nós dois jogamos {}'.format(ppt))
        elif ppt == pa:
            print('Você Perdeu! Eu joguei {} e você jogou {}.'.format(ppt, pe))
        else:
            print('Você ganhou! Eu joguei {} e você jogou {}.'.format(ppt, pe))
    elif ch == 2:
        if ppt == pa:
            print('Houve um empate! Nós dois jogamos {}'.format(ppt))
        elif ppt == pe:
            print('Você Perdeu! Eu joguei {} e você jogou {}.'.format(ppt, pa))
        else:
            print('Você ganhou! Eu joguei {} e você jogou {}.'.format(ppt, pa))

    else:
        if ppt == te:
            print('Houve um empate! Nós dois jogamos {}'.format(ppt))
        elif ppt == pe:
            print('Você Perdeu! Eu joguei {} e você jogou {}.'.format(ppt, te))
        else:
            print('Você ganhou! Eu joguei {} e você jogou {}.'.format(ppt, te))
    for c in range(0,4):
        print('.')
        sleep(0.5)
    d = str(input('Deseja jogar novamente? [S]/[N]:').upper()).strip()
    for c in range(0,4):
        print('.')
        sleep(0.5)