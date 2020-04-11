#nome em letras maiuscula, em minusculas,
# quantas letras sem o espaço equantas letras tem o primeiro nome

print('')
nome = (input('Qual é o seu nome completo? '))
print('')
name = (nome.strip())
print('Aqui está seu nome com todas as letras maiúsculas: {};'.format((name.upper())))
print('')
print('Aqui está seu nome com todas as letras mainúsculas: {};'.format((name.lower())))
print('')
nsl = (name.split())
ns = (len(''.join(nsl)))
print('O seu nome (sem contar os espaços) possui {} letras;'.format(ns))
print('')
print('E por fim seu primeiro nome possui {} letras.'.format(len(nsl[0])))


