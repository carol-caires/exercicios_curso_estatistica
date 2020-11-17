import numpy as np
import statistics
from scipy import stats
import math

dados = np.array([150, 151, 152, 152, 153, 154, 155, 155, 155, 155, 156, 156, 156,
                  157, 158, 158, 160, 160, 160, 160, 160, 161, 161, 161, 161, 162,
                  163, 163, 164, 164, 164, 165, 166, 167, 168, 168, 169, 170, 172,
                  173])


# Média aritmética manual
media1 = dados.sum() / len(dados)

# Média aritmética usando biblioteca padrão
media2 = dados.mean()

# Média aritmética usando statistics
media3 = statistics.mean(dados)

print("Média:\n", media1, media2, media3)

# Moda usando statistics

moda1 = statistics.mode(dados)

# Moda usando stats

moda2 = stats.mode(dados)

print("Moda:\n", moda1, moda2)

# Mediana

dados_impar = [150, 151, 152, 152, 153, 154, 155, 155, 155]

# Cálculo manual de mediana - número de elementos ímpar
posicao = len(dados_impar) / 2
posicao = math.ceil(posicao)
mediana1 = dados_impar[posicao - 1]

# Cálculo manual de mediana - número de elementos par
posicao = len(dados) // 2
mediana2 = (dados[posicao - 1] + dados[posicao]) / 2

print("Mediana  - Cálculo manual:\n", mediana1, mediana2)

# Mediana usando numpy
mediana1 = np.median(dados_impar)
mediana2 = np.median(dados)

print("Mediana  - Numpy:\n", mediana1, mediana2)

# Mediana usando statistics
mediana1 = statistics.median(dados_impar)
mediana2 = statistics.median(dados)

print("Mediana  - Statistics:\n", mediana1, mediana2)