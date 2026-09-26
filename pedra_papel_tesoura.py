from os import system
import random #random para gerar a escolha do computador
system('cls')

continua = 'S'

while continua == 'S':

    computador=random.randint(0,2) #computador vai escolher um número aleatório entre 0 e 2
    jogador=int(input('''Opções:
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA
    Escolha uma opção: ''')) #jogador escolhe um número entre 0 e 2
    system('cls') #limpa a tela



    if jogador >= 0 and jogador <=2:

        peças = ('PEDRA', 'PAPEL', 'TESOURA')
        print(f'Computador escolheu {peças[computador]}')
        print(f'Jogador escolheu {peças[jogador]}')

        tabela = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]] #tabela de resultados
        resultado = tabela[jogador][computador] #resultado do jogo

        if resultado == 0:
            print("Empate!")
        elif resultado == 1:
            print("Você venceu a Máquina!")
        else:
            print("Você perdeu para a Máquina!")

    else:
        print("Jogador escolheu a opção Inválida!")

    continua = input("Deseja jogar novamente? [S/N] ").upper()
