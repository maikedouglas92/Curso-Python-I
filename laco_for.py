from os import system
system('cls')

numero = int(input('Informe um número maior que 0: '))
#Verifica se o numero é positivo
if numero <= 0:
    print('Numero Invalido!')

else:
    #Iniciando laço For
    for i in range(numero):
        print(f'Valor da variaveis i: (i)')
        time.sleep(2)