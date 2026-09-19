#conversor de temperatura

print('Bem-vindo ao conversor de temperatura!')
print('Escolha a opção desejada: \n1 - Celsius para Fahrenheit \n2 - Fahrenheit para Celsius')
escolha = int(input("Digite a opção desejada: "))

if escolha == 1:
    celsius = float(input('Digite a temperatura em Celsius: '))
    fahrenheit = (celsius * 1.8) + 32
    print(f'A temperatura em Fahrenheit é: {fahrenheit:.2f}')
elif escolha == 2:
    fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
    celsius = (fahrenheit - 32) / 1.8
    print(f'A temperatura em Celsius é: {celsius:.2f}')
elif escolha == 3:
    kelvin = float(input('Digite a temperatura em Kelvin: '))
    celsius = kelvin + 273.15
    print(f'A temperatura em Celsius é: {celsius:.2f}')

else:
    print('Opção inválida')
