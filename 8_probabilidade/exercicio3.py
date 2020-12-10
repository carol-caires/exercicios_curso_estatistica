import math

from scipy import stats

"""
    70% das pessoas que compraram o livro de Python são mulheres. Se 10 leitores forem selecionados randomicamente,
    qual a probabilidade de selecionarmos 7 mulheres?
"""

''' Cálculo manual '''

n = 10  # quantidade de experimentos
x = 7  # quantidade de sucessos desejada
p = 0.7  # probabilidade de sucesso por experimento

prob = (math.factorial(n)) / (math.factorial(x) * math.factorial(n - x)) * math.pow(p, x) * math.pow(1 - p, n - x)
# print("A probabilidade de selecionar %d mulheres é de %.2f%%" % (x, prob * 100))

''' Cálculo usando scipy '''

prob2 = stats.binom.pmf(x, n, p)
print("A probabilidade de selecionar %d mulheres é de %.2f%%" % (x, prob2 * 100))

"""
    Em uma linha de produção de uma fábrica de parafusos, a probabilidade de obter um parafuso defeituoso é 0,05. 
    Tendo uma amostra de 50 peças, qual a probabilidade de obter:
    - Um parafuso defeituoso
    - Nenhum parafuso defeituoso
"""

n = 50  # quantidade de experimentos
x = 1  # quantidade de sucessos desejada
p = 0.05  # probabilidade de sucesso por experimento

prob3 = stats.binom.pmf(x, n, p)
print("A probabilidade de selecionar %d parafuso defeituoso é de %.2f%%" % (x, prob3 * 100))

x = 0
prob4 = stats.binom.pmf(x, n, p)
print("A probabilidade de selecionar nenhum parafuso defeituoso é de %.2f%%" % (prob4 * 100))
