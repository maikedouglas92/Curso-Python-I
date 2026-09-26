from os import system
system('cls')
import time

# Inica contagem do "Multiplicador"
for ii in range(1, 11):
    print(f"Tabuada do {ii}:")
    for i in range(1, 11):
# Monta a expressão de Multiplicção
        print(f"{ii} x {i} = {ii * i}")
        time.sleep(0.5)
    print('')
