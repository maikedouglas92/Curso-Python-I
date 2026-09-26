from os import system
system('cls')

nome = []
total = int(input('Quantos nomes deseja cadastrar? '))

for i in range(0,total):
    nome.append(input('Digite um nome: '))
    system('cls')


for i in range(0,total):
    print(f'{i} - {nome[i]}')
