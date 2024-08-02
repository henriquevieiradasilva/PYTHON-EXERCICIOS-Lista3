"""

8) Escreva um programa que leia uma idade de uma pessoa e verifique se ela é maior de idade ou não. Considere a idade
mínima para ser maior de idade como 18 anos.

"""
while True:
    try:
        idade = int(input('Digite quantos ANOS você tem:\n'))
        if idade >= 0 and idade <= 130:
            break
        print('\nPor favor, digite um valor válido.')
    except:
        print('\nPor favor, digite um valor válido.')

if idade >= 18:
    print('Parabéns, você já É maior de idade.')
else:
    print('Você ainda NÃO É maior de idade.')

idade = 0