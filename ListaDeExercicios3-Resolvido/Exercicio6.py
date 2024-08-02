"""

6) Faça um programa para solicitar que o usuário digite um número inteiro qualquer. Indique se o número digitado é
positivo ou negativo.

"""
while True:
    try:
        numeroDigitado = int(input('Digite um NÚMERO INTEIRO qualquer:\n'))
        break
    except:
        print('\nPor favor, digite um valor válido.')

if numeroDigitado > 0:
    print(f'O número {numeroDigitado} é um número POSITIVO')
elif numeroDigitado < 0:
    print(f'O número {numeroDigitado} é um número NEGATIVO')
else:
    print(f'O número {numeroDigitado} é um número NEUTRO, por ser o número ZERO')

numeroDigitado = 0