import math

from scipy import stats

"""
    Em uma linha de produção de uma fábrica de parafusos, a probabilidade é de obter 0,05 defeitos por UNIDADE. 
    Qual a probabilidade de uma unidade apresentar:

    - Um defeito
    - Nenhum defeito
"""

media = 0.05
x = 1

print("Um defeito: %.2f%%" % (math.pow(math.e, -media) * (math.pow(media, x) / math.factorial(x)) * 100))

x = 0

print("Zero defeito: %.2f%%" % (math.pow(math.e, -media) * (math.pow(media, x) / math.factorial(x)) * 100))

"""
    Um vendedor de uma loja vende em média 50 produtos por dia. Qual a probabilidade de vender somente 5 produtos no próximo dia?
"""

media = 50
x = 5

print("Probabilidade de vender apenas 5 produtos: %.14f%%" % (math.pow(math.e, -media) * (math.pow(media, x) / math.factorial(x)) * 100))

''' Usando scipy '''
stats.poisson.pmf(x, media)