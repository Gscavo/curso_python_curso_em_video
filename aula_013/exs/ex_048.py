#Somátorio números divisiveis por 3 até 500:
from time import sleep

n = 0

for c in range(1, 500, 2):
    if c % 3 == 0:
        n = (n+c)
        print(c)
        sleep(0.2)
print('''A somátoria de todos os Números de 1 até 500
cujo são impares e divisiveis por 3 é: {}{}'''.format('\033[1;33m', n))