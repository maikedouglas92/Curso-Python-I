from os import system
system('cls')

clientes = []
telefones = []

# Inicializamos a variável vazia para entrar no laço
opcao = ''

while opcao != 'X':
    system('cls')
    nome = input('Digite o nome do cliente: ')
    telefone = input('Digite o telefone do cliente: ')

    clientes.append(nome)
    telefones.append(telefone)

    system('cls')
    print('Cadastro realizado com sucesso!')
    opcao = input('Aperte X para finalizar ou qualquer outra tecla para continuar: ').upper()

    system('cls')
    
    # Exibe a lista atualizada de clientes cadastrados até agora
    print('--- Clientes Cadastrados ---')
    total = len(clientes) # Descobre o tamanho atual da lista
    for i in range(0, total):
        print(f'{i} - Nome = {clientes[i]} - Telefone = {telefones[i]}')
        
    print('----------------------------')
    input('\nPressione Enter para continuar...') # Pausa para o usuário conseguir ler a lista antes da tela limpar

