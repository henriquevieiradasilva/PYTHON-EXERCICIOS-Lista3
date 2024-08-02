"""

5) Faça um programa para solicitar que o usuário digite um número inteiro qualquer. Indique se o número digitado é par
ou ímpar

"""
while True:
    try:
        numeroDigitado = int(input('Digite um NÚMERO INTEIRO qualquer:\n'))
        break
    except:
        print('\nPor favor, digite um valor válido.')

if numeroDigitado % 2 == 0:
    print(f'O número {numeroDigitado} é PAR')
else:
    print(f'O número {numeroDigitado} é IMPAR')

numeroDigitado = 0