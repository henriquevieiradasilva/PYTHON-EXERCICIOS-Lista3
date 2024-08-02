"""

9) Construa um programa para determinar se um número qualquer inteiro é um quadrado perfeito. Antes de calcular, caso o
número seja negativo, multiplique-o por -1.

"""
import math
while True:
    try:
        numeroDigitado = int(input('Digite um NÚMERO INTEIRO qualquer:\n'))
        if numeroDigitado < 0:
            numeroDigitado *= -1
        break
    except:
        print('\nPor favor, digite um valor válido.')

raizNumeroDigitado = int(math.sqrt(numeroDigitado))
numeroDigitadoConfirmacao = raizNumeroDigitado * raizNumeroDigitado

if numeroDigitado == numeroDigitadoConfirmacao:
    print(f'O número {numeroDigitado} É um QUADRADO PERFEITO do número {raizNumeroDigitado}')
else:
    print(f'O número {numeroDigitado} NÃO É um QUADRADO PERFEITO')

numeroDigitado = 0
raizNumeroDigitado = 0
numeroDigitadoConfirmacao = 0