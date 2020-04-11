''' Leitura de vários Números
    Para com o número Sim ou Não
    -Média entre eles
    -Maior e menor número '''
x = 0
n = 0
ma = 0
me = 0
md = 0
media = 0
d = 'S'

while d not in 'N':
    n += 1
    x = int(input('Número: '))
    if n == 1:
        ma = x
        me = x
    else:
        if x > ma:
            ma = x
        if x < me :
            me = x
    md += x
    d = str(input(('Deseja continuar?[S]/[N] ')).upper()).strip() [0]\

media = (md/n)
print('A media do números digitados é {:.1f}, sendo o Maior número {} e o Menor {}.'.format(media, ma, me))