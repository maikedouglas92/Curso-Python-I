# Calculadora INSS 2026

salario = input('Digite seu salário: R$ ')
salario = float(salario.replace(',', '.'))

if salario <= 1621:
    aliquota = 0.075
    parcela = 0

elif salario <= 2430:
    aliquota = 0.09
    parcela = 24.32

elif salario <= 3240:
    aliquota = 0.12
    parcela = 111.41

elif salario <= 8475.55:
    aliquota = 0.14
    parcela = 198.50

else:
    aliquota = 0.14
    parcela = 198.50

inss = salario * aliquota - parcela

print(f'\nSalário: R$ {salario:.2f}')
print(f'Alíquota: {aliquota * 100:.1f}%')
print(f'Desconto do INSS: R$ {inss:.2f}')
salario_apos_inss = salario - inss
print(f'Salário após INSS: R$ {salario - inss:.2f}')

#Calculo de imposto de renda
if salario_apos_inss <= 2259.20:
    aliquota_ir = 0
    parcela_ir = 0

elif salario_apos_inss <= 2826.65:
    aliquota_ir = 0.075
    parcela_ir = 169.44

elif salario_apos_inss <= 3751.05:
    aliquota_ir = 0.15
    parcela_ir = 381.44

elif salario_apos_inss <= 4664.68:
    aliquota_ir = 0.225
    parcela_ir = 662.77

else:
    aliquota_ir = 0.275
    parcela_ir = 896.00

ir = salario_apos_inss * aliquota_ir - parcela_ir

# Evita que o imposto fique negativo
if ir < 0:
    ir = 0

salario_liquido = salario_apos_inss - ir

print(f'\n--- Imposto de Renda ---')
print(f'Alíquota IR: {aliquota_ir * 100:.1f}%')
print(f'Desconto do IR: R$ {ir:.2f}')
print(f'Salário líquido: R$ {salario_liquido:.2f}')