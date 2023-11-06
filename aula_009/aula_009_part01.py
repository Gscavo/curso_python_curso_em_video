print('')
print('{:=^100}'.format('Cadeias de texto!'))
print('')
#É uma string <----
#'Aparecem entre aspas simples ou duplas.'
#Fatiamento de frases: Divir a frase em pedaços
#Ex.: 'Python é dificil!'
#      0123456789... -->Cada letra representa um número,
#sendo a primeira 0.
ex = 'Exemplo da aula.'
print()
print(ex)
print('')
print(ex[0:7])
print(' ', ex[8:10])
print('', ex[11:15])
print('')
print(ex[0:15:3])
#Esse 3 no final sinifica que vai pulando a frase de 3 em 3 letras
print('')
print(ex[:7])
print(ex[11:])
print(ex[::3])
print(ex[3])
#                                      Análise --> Analise da frase

#LEN(frase)-> analisa o tamanho da frase

#frase.COUNT('x')-> vai contar quantos x possuem na frase/// se colocar frase.count.('x',0,13)-> vai contar quantos o tem de 0 a 12

#frase.FIND('xyz')-> vai indicar a posição que se inicia o xyz

#'xyz' IN frase-> diz se existe ou não xyz na frase


#                                          Transformação

#frase.REPLACE('xyz', 'abc')-> troca todos os 'xyz' por 'abc'

#frase.UPPER() -> põe a frase em maiscúla

#frase.LOWER() -> póe em minuscula

#frase.CAPITALIZE()-> vai por tudo em minusculo e o a primeira letra da frase em maiuscula

#frase.TITLE() -> vai por tudo em minuscula e as primeiras letras das palavras vao pra maiusculas

#frase.STRIP() -> remove os espaços excedentes(começo e fim) ex.: '   Guilherme cavo  '---->'Guilherme cavo'

#frase.RSRTIP() -> remove os espaços excendentes da direita

#frase.LSTRIP() -> mesma ideia do rstrip, porem pra esquerda

#                                        Divisão

#frase.SPLIT()-> divide as palavras e cria uma lista com as palavras []

#                                        Junção

# '-'.JOIN(frase) -> Junta as palavras usando oq estiver entre as aspas