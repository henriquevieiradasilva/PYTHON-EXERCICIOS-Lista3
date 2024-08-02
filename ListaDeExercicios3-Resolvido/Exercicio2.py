"""

2) Um produto tem um desconto sobre seu preço, considerando o dia do mês em que foi comprado: se for na primeira
quinzena, o desconto é de 8%; se for na segunda quinzena, o desconto é de 6%. Mostre o preço do produto com desconto.

"""
while True:
    try:
        diaDoMes = int(input('Qual o DIA atual?\n'))
        if diaDoMes > 0 and diaDoMes < 32:
            break
        print('\nPor favor, digite um número válido')
    except:
        print('\nPor favor, digite um número válido')

while True:
    try:
        valorProduto = float(input('Qual o valor atual do PRODUTO?\n'))
        if valorProduto > 0:
            break
        print('\nPor favor, digite um número válido')
    except:
        print('\nPor favor, digite um número válido')

if diaDoMes <= 15:
    valorProduto -= valorProduto * 0.08
else:
    valorProduto -= valorProduto * 0.06
print(f'Seu produto agora tem o valor de {valorProduto:.2f}')

diaDoMes = 0
valorProduto = 0