#Converter real , dolar, euro

escolha = int(input("Digite a opção desejada: \n1 - Dolar \n2 - Euro\n"))
valor = float(input("Digite o valor em reais: "))

if escolha == 1:
    print("Você escolheu a moeda Dolar")
    dolar = valor / 5.13
    print(f'O valor em Dolar é de: {dolar:.2f}')
elif escolha == 2:
    print("Você escolheu a moeda Euro")
    euro = valor / 5.95
    print(f'O valor em Euro é de: {euro:.2f}')
else:
    print("Opção inválida")
