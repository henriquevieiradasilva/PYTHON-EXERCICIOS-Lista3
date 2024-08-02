"""

3) Calcule e mostre as raízes reais de uma função polinomial de segundo grau.

"""
import math
print('Estrutura básica de uma FUNÇÃO POLINOMIAL:')
print('f(x) = Ax² + Bx + C')

while True:
    try:
        valorA = float(input('Digite o valor de "A"\n'))
        if valorA != 0:
            break
        print('\nO valor de "A" deve ser diferente de 0')
    except:
        print('\nDigite um valor válido para "A"')

while True:
    try:
        valorB = float(input('Digite o valor de "B"\n'))
        break
    except:
        print('\nDigite um valor válido para "B"')

while True:
    try:
        valorC = float(input('Digite o valor de "C"\n'))
        break
    except:
        print('\nDigite um valor válido para "C"')

try:
    delta = math.sqrt(valorB ** 2 - 4 * valorA * valorC)
    primeiraRaiz = (-valorB + delta) / (2 * valorA)
    segundaRaiz = (-valorB - delta) / (2 * valorA)
    resposta = 'A PRIMEIRA RAIZ vale {} e a SEGUNDA RAIZ vale {}'
    print(resposta.format(primeiraRaiz, segundaRaiz))
except:
    print('Essa função não possui raizes reais.')

valorA = 0
valorB = 0
valorC = 0
delta = 0
primeiraRaiz = 0
segundaRaiz = 0
resposta = ''

