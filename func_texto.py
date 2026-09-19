# Funções para trabalhar com textos
from os import system
system('cls')
nomecompleto = input('Digite seu nome completo: ')

#contando o número de caracteres
#Strip tira os espaços do começo e do final da string
print(f'O seu nome completo tem {len(nomecompleto.strip())} caracteres')
#sem o espaço strip tira os espaços 
print('Texto maisculo: ', nomecompleto.upper())
#deixar tudo minusculo
print('Texto minusculo: ', nomecompleto.lower())
#capitalizar a primeira letra da primeira palavra
print('Texto capitalizado: ', nomecompleto.capitalize())
#capitalize só que com toda palavra capitalizada
print('Texto com cada palavra capitalizada: ', nomecompleto.title())

#pegar o primeiro nome
espaco = nomecompleto.find(' ')
print('Primeiro nome: ', nomecompleto[0:espaco])


#Vou usar o replace para remover espaços do meio
print('Nome sem espaços: ', nomecompleto.replace(' ', ''))
#Agora com o len eu consigo contar quantos caracteres tem o nome sem espaços
print(f'O seu nome completo tem {len(nomecompleto.replace(" ", ""))} caracteres')

#Operadores Lógicos:
# != diferente que
# == iqual que
# < menor que
# > maior que
# >= maior ou igual que
# <= menor ou igual que








 