import time  # Importação necessária para o time.sleep funcionar
from os import system

system("cls")  # Limpa a tela (apenas no Windows)

numero = int(input("Informe um número maior que 0: "))

# Verifica se o numero é positivo
if numero <= 0:
    print("Numero Invalido!")
else:
    # Iniciando laço For
    for i in range(numero):
        print(f"Valor da variavel i: {i}")  # Corrigido para {i}
        time.sleep(2)
