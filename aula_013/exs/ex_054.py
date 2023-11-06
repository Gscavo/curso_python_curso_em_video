#Maioridade:
from datetime import date

year = int(date.today().year)

s = 0

for c in range(0,6):
    birth = int(input('Digite aqui o ano de nascimento de alguém: '))
    if (year-birth) >= 21:
        s = (s+1)

print('Das 6 pessoas, {} atingiram a maioridade.'.format(s))