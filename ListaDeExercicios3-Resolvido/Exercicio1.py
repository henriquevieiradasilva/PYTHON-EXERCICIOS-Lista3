"""

1) Um funcionário recebe um salário mensal em sua empresa. Caso esse salário seja maior que 5000, ele deverá receber um
aumento de 12%; caso contrário, o aumento será de 15%. Mostre o salário com aumento.

"""
while True:
    try:
        salario = float(input('Qual o valor do seu SALÁRIO atual?\n'))
        if salario > 0:
            break
        print('\nPor favor, digite um número válido.')
    except:
        print('\nPor favor, digite um número válido.')

if salario > 5000:
    salario += salario * 0.12
else:
    salario += salario * 0.15

print(f'Seu NOVO SALÁRIO é de {salario:.2f}')

salario = 0