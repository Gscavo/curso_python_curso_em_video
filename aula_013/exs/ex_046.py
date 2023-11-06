from time import sleep
print('{:_^100}'.format('!!Lançamento Fogos de Artifício!!'))
for c in range(10, 0, -1):
    print('', c)
    sleep(1)
print('{}!BOOM!{}'.format('\033[1;31m', '\033[m'))