"""

10) Faça um programa para calcular quanto a prefeitura de uma cidade precisa investir por habitante, baseado em um valor
base, digitado pelo usuário. Se a cidade tiver mais de 10.000 habitantes precisa investir, por cidadão, o valor base
aumentado em 20%; caso contrário, pode investir o valor base aumentado em 15%.

"""
while True:
    try:
        valorBase = float(input('Digite o VALOR BASE do investimento por habitante:\n'))
        if valorBase > 0:
            break
        print('\nPor favor, digite um valor válido.')
    except:
        print('\nPor favor, digite um valor válido.')

while True:
    try:
        quantidadeHabitantes = int(input('Digite o total de HABITANTES da cidade:\n'))
        if quantidadeHabitantes >= 100:
            break
        print('\nPor favor, digite um valor válido (mínimo 100 habitantes).')
    except:
        print('\nPor favor, digite um valor válido.')

if quantidadeHabitantes > 10000:
    valorBase += valorBase * 0.20
else:
    valorBase += valorBase * 0.15

print(f'O valor do investimento POR HABITANTE é de {valorBase:.2f} e o TOTAL é de {valorBase * quantidadeHabitantes:.2f}')

valorBase = 0
quantidadeHabitantes = 0