from os import system
system('cls')
import time

#Inicia a contagem Multiplicando
    
for i in range(1,11):
# Limpa a variável linha 
    linha = ""
    for ii in range(1,11):
# Monta a expressão de Multiplicção
#":>4" totaliza04 caractere , completando com espaço vazio à esquerda
        linha += f'{i*ii: >4} '
# Mostra o resultado da Tabuada

    print(linha)
time.sleep(0.5)