from os import system
system('cls')


def Somar(a,b):
                print(f'Soma:{a}+{b} = {a+b}')

def Subtrair(a,b):
                print(f'Subtração:{a}-{b} = {a-b}')

def Multiplicar(a,b):
                print(f'Multiplicação:{a}*{b} = {a*b}')

def Dividir(a,b):
    try:
        print(f'Divisão:{a}/{b} = {a/b}')
    except :
        print('Erro: Divisão por zero não é permitida.')

opcao = ''

while opcao.upper() != 'X':
        system('cls')

        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))

        opcao = input('''
        Opções:
        [1] - Somar
        [2] - Subtrair
        [3] - Multiplicar
        [4] - Dividir
        Escolha uma opção acima: ''')

        if opcao == '1':
            Somar(num1,num2)
        elif opcao == '2':
            Subtrair(num1,num2)
        elif opcao == '3':
            Multiplicar(num1,num2)
        elif opcao == '4':
            Dividir(num1,num2)
        else:
            print('Opção inválida!')


        opcao = input('aperte o X para finalizar ou qualquer tecla para continuar: ')

