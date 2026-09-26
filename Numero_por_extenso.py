from os import system
system('cls')

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')
dez = ('dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')
dezena = ('vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa')

numero = int(input('Digite um número de 0 a 99: '))

if numero >= 0 and numero <= 99:

    if numero < 10:
        print(numeros[numero])
    elif numero < 20:
        print(dez[numero-10])
    else:
        dezena_index = (numero // 10) - 2
        unidade = numero % 10
        if unidade == 0:
            print(dezena[dezena_index])
        else:
            print(f"{dezena[dezena_index]} e {numeros[unidade]}")
else:
    print("Numero inválido!")