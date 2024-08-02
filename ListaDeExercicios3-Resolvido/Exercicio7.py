"""

7) Construa um programa para solicitar a entrada de três números inteiros, N1, N2 e N3. Coloque os valores em ordem
numérica crescente, ou seja, o menor em N1, o maior em N3 e o outro número em N2. Exiba os números N1, N2 e N3.

"""
while True:
    try:
        numeroDigitado = int(input('Digite o PRIMEIRO número:\n'))
        numero1 = numeroDigitado
        break
    except:
        print('\nPor favor, digite um valor válido.')

while True:
    try:
        numeroDigitado = int(input('Digite o SEGUNDO número:\n'))
        if numero1 < numeroDigitado:
            numero2 = numeroDigitado
        else:
            numero2 = numero1
            numero1 = numeroDigitado
        break
    except:
        print('\nPor favor, digite um valor válido.')

while True:
    try:
        numeroDigitado = int(input('Digite o TERCEIRO número:\n'))
        if numeroDigitado >= numero2:
            numero3 = numeroDigitado
        elif numeroDigitado > numero1:
            numero3 = numero2
            numero2 = numeroDigitado
        else:
            numero3 = numero2
            numero2 = numero1
            numero1 = numeroDigitado
        break
    except:
        print('\nPor favor, digite um valor válido.')

print(f'Em ordem CRESCENTE os números ficam: {numero1}, {numero2}, {numero3}')

numeroDigitado = 0
numero1 = 0
numero2 = 0
numero3 = 0