from os import system
from datetime import datetime  # Importando o módulo de data e hora

system('cls')

# Iniciando a classe Serviço
class Servico:
    # Construtor/Inicializer da classe
    def __init__(self, descricao, preco):
        self.descricao = descricao
        self.preco = preco
        # Captura a data e hora atual no momento da criação do objeto
        self.data_cadastro = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    # Método para exibir os dados do serviço
    def exibir_dados(self):
        print(f'Descrição: {self.descricao}')
        print(f'Preço: R${self.preco:.2f}')
        print(f'Cadastrado em: {self.data_cadastro}')  # Exibe a data/hora na tela

    # Método para salvar dados TXT
    def salvar_dados(self):
        with open('servicos.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'Data/Hora: {self.data_cadastro}\n')  # Grava no arquivo
            arquivo.write(f'Descrição: {self.descricao}\n')
            arquivo.write(f'Preço: R${self.preco:.2f}\n')
            arquivo.write('-' * 40 + '\n')

# Iniciando o código principal
print(' == CADASTRO DE SERVIÇOS == ')

continuar = 'S'
while continuar.upper() != 'X':
    descricao = input('Informe a descrição do serviço: ')
    preco = input('Informe o preço do serviço: ')
    
    try:
        preco = float(preco)
    except ValueError:
        print('Preço inválido. Por favor, insira um número válido.')
        continue

    system('cls')

    # Criando uma instância da classe Serviço
    servico = Servico(descricao, preco)
    
    # Salvando os dados no arquivo TXT
    servico.salvar_dados()
    
    # Exibindo os dados do serviço
    servico.exibir_dados()
    
    print('-' * 40)
    continuar = input('Tecle "Enter" para continuar ou "X" para sair: ')
    system('cls')
