"""
    Os intervalos de confiança definem a margem de erro de um parâmetro de uma amostragem em relação à população.
    Ou seja, de acordo com a porcentagem de confiança `x` escolhida (normalmente 95% ou 99%),
    calculamos uma margem inferior de n unidades abaixo e acima da média e isso significa que `x`% da população, com certeza,
    terá a média daquele parâmetro entre as margens inferior e superior
"""

import numpy as np
from scipy.stats import norm
from scipy import stats
import math

dados = np.array([126., 129.5, 133., 133., 136.5, 136.5, 140., 140., 140.,
                  140., 143.5, 143.5, 143.5, 143.5, 143.5, 143.5, 147., 147.,
                  147., 147., 147., 147., 147., 150.5, 150.5, 150.5, 150.5,
                  150.5, 150.5, 150.5, 150.5, 154., 154., 154., 154., 154.,
                  154., 154., 154., 154., 157.5, 157.5, 157.5, 157.5, 157.5,
                  157.5, 157.5, 157.5, 157.5, 157.5, 161., 161., 161., 161.,
                  161., 161., 161., 161., 161., 161., 164.5, 164.5, 164.5,
                  164.5, 164.5, 164.5, 164.5, 164.5, 164.5, 168., 168., 168.,
                  168., 168., 168., 168., 168., 171.5, 171.5, 171.5, 171.5,
                  171.5, 171.5, 171.5, 175., 175., 175., 175., 175., 175.,
                  178.5, 178.5, 178.5, 178.5, 182., 182., 185.5, 185.5, 189., 192.5])

n = len(dados)
media = np.mean(dados)
desvio_padrao = np.std(dados)

''' Cálculo manual '''

alpha = 0.05 / 2  # 0.05 é 1 - a porcentagem de confiabilidade desejada (0,95)
z = norm.ppf(1 - alpha)  # obtém o número correspondente na tabela Z
x_inferior = media - z * (desvio_padrao / math.sqrt(n))
x_superior = media + z * (desvio_padrao / math.sqrt(n))

# margem_erro = abs(media - x_superior)
# print("A margem de erro das alturas é de %.2f centímetros" % margem_erro)

''' Cálculo com scipy '''

err_padrao = stats.sem(dados)  # erro padrão
intervalos = norm.interval(0.95, media, stats.sem(dados))
margem_erro = media - intervalos[0]

print("A margem de erro das alturas é de %.2f centímetros" % margem_erro)