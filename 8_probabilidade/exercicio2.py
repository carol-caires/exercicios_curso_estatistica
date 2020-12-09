from scipy.stats import norm

"""
    Uma empresa fez um concurso para seleção de novos funcionários. A prova tinha 50 questões e o Pedro acertou 40 questões. 
    Considerando uma distribuição normal com média 24 e desvio padrão de 8, quais são as chances dele ser contratado?
"""

qtd_acertos = 40
media = 24
desvio_padrao = 8

''' usando scipy '''
print("A probabilidade de Pedro ser contratado é de %.2f%%" % (norm.cdf(qtd_acertos, media, desvio_padrao) * 100))

''' cálculo manual '''
padronizado = (qtd_acertos - media) / desvio_padrao
# essa função norm.cdf chamada dessa forma retorna o valor correspondente da z-table, o que já é a probabilidade
# print("A probabilidade de Pedro ser contratado é de %.2f%%" % (norm.cdf(padronizado) * 100))

"""
    A vida útil de uma marca de pneus é representada por uma distribuição normal com média de 38.000 Km e desvio padrão de 3.000 Km
    1. Qual a probabilidade de que um pneu escolhido aleatoriamente tenha vida útil de 35.000 Km?
    2. Qual a probabilidade de que ele dure mais do que 44.000 Km?
"""

media = 38000
desvio_padrao = 3000

vu1 = 35000
vu2 = 44000

print("A probabilidade de chegar a 35k é de %.2f%%" % (norm.sf(vu1, media, desvio_padrao) * 100))
print("A probabilidade de chegar a 44k é de %.2f%%" % (norm.sf(vu2, media, desvio_padrao) * 100))
