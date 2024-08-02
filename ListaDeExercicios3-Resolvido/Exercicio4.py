"""

4) Em uma escola, um aluno pode ser reprovado se tiver mais de 25% de faltas em relação às aulas dadas. Faça um programa
para solicitar o número de aulas dadas e o número de faltas do aluno e indique se ele foi aprovado ou não, bem como o
percentual de faltas.

"""
while True:
    try:
        totalDeAulas = int(input('Digite o total de AULAS:\n'))
        if totalDeAulas > 0:
            break
        print('\nPor favor, digite um número válido.')
    except:
        print('\nPor favor, digite um número válido.')

while True:
    try:
        totalDeFaltas = int(input('Digite o total de FALTAS:\n'))
        if totalDeFaltas >= 0:
            break
        print('\nPor favor, digite um número válido.')
    except:
        print('\nPor favor, digite um número válido.')

totalDeFaltas = totalDeFaltas / totalDeAulas * 100

if totalDeFaltas > 25:
    print(f'Você está REPROVADO por excesso de FALTAS, com o total de {totalDeFaltas:.1f}%')
else:
    print(f'Você está APROVADO, com o total de FALTAS de {totalDeFaltas:.1f}%')

totalDeFaltas = 0
totalDeAulas = 0