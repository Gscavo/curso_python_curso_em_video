#Sequência de Fibonacci:

n = int(input('Você deseja ver quantos números da sequencia de Fibonacci: '))
c = -1
a1 = 0
a2 = 1
f = 0

#Algoritmo
while c < (n-1):
   c += 1
   f = a1+a2
   a1 = a2
   a2 = f
   print(f, end=' - ')
print('END')