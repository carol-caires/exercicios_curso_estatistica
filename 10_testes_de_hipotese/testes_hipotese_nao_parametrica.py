from testes_normalidade import resultados_naive_cv, resultados_logistica_cv, resultados_forest_cv
from scipy.stats import friedmanchisquare
from scipy.stats import wilcoxon

"""
    Quando os dados disponíveis não estão em uma distribuição normal ou você não tem disponível os testes de normalidade
    ou ainda acredita que a normalidade dos dados foi corrompida, podemos aplicar testes de hipótese da estatística não-paramétrica
    para avaliar se existe diferença estatística ou não entre dois ou mais conjuntos de dados.
    
    Abaixo, aplicamos o teste de Wilcoxon Signed-Rank para comparar os resultados dos 3 algoritmos e ver se há diferença
    estatística entre eles.
"""

_, p = wilcoxon(resultados_naive_cv, resultados_logistica_cv)
print(p)

_, p = wilcoxon(resultados_naive_cv, resultados_forest_cv)
print(p)

_, p = wilcoxon(resultados_logistica_cv, resultados_forest_cv)
print(p)

_, p = friedmanchisquare(resultados_naive_cv, resultados_logistica_cv, resultados_forest_cv)
print(p)

''' No caso, os 3 resultados acima são menores do que o alpha (0.05) e indica que existe diferença estatística entre eles,
 logo a média dos resultados é relevante para avaliar se o algoritmo é melhor do que o outro para aquele dataset ou não '''
