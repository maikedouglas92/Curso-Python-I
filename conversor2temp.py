

print('Oi, vamos para o programa')

escolha = int(input('escolha uma opacao de 1 a 4: '))

if escolha == 1:
    celsius = float(input('Digite uma temperatura em Celsius: '))
    fahrenheit = (celsius * 1.8) + 32
    print(f'A temp em Fahrenheit é: {fahrenheit:.2f}')
elif escolha == 2:
    fahrenheit = float(input('Digite uma temp em Fahrenheit: '))
    celsius = (fahrenheit - 32) / 1.8
    print(f'A temp em Celsius é: {celsius:.2f}')
elif escolha == 3:
    kelvin = float(input('Digite uma temp em Kelvin: '))
    celsius = kelvin + 273.15
    print(f'A temp em Celsius é: {celsius:.2f}')
elif escolha == 4:
    kelvin = float(input('Digite uma temp em Kelvin: '))
    fahrenheit = (kelvin - 273.15) * 1.8 + 32
    print(f'A temp em Fahrenheit é: {fahrenheit:.2f}')
else:
    print('opcao invalida')