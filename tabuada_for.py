from os import system
system('cls')

numero = int(input("Digite um número: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {numero * i}")
