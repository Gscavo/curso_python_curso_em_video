from random import randint
from emoji import emojize
print('')
print('')
name = str(input('Olá eu sou o Pensante, como você se chama? '))
print('')
print('É um prazer te conhecer {}!'.format(name))
p = input('Você gostaria de brincar comigo?').upper()
if p == 'SIM' or 'S':
    print('OK! Então vamos lá.')
    print('')
    print('O seu objetivo é descobrir o número que eu estou pensando.')
    print('P.S: Já que eu gostei de você vou te dar uma dica:')
    print('')
    print('-O número está entre 0 e 5.')
    print('')
    num1 = randint(0,5)
    num = int(input('Qual número eu estou pensando? '))
    print('')
    if num == num1:
        print(emojize('==!VOCÊ VENCEU!:tired_face:==', use_aliases=True))
        print('Foi um prazer jogar com você!')
    else:
        print(emojize('Você perdeu :satisfied:', use_aliases=True))
        print('')
        num2 = int(input('Eu vou deixar você tentar novamente: '))
        if num2 == num1:
            print(emojize('==!VOCÊ VENCEU!:tired_face:==', use_aliases=True))
            print('Foi um prazer jogar com você!')
        else:
            print(emojize('Você perdeu :satisfied:', use_aliases=True))
            print('Sem segundas chances desta vez!')
            print('Até a próxima!')
else:
    print('Ok! Então Adios')