while True:
    try:
        base = float(input("Digite a base do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        area = base * altura
        print(f"A área do retângulo é: {area}")
        break
    except ValueError:
        print("Por favor, insira um número válido.")
