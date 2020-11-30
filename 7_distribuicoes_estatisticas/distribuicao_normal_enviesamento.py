'''
    Chama-se de distribuição normal quando a média, moda e mediana de um atributo estão no centro da distribuição, bem
    próximos um dos outros.
    Enviesamento positivo é quando a média está acima do valor da moda e da mediana. E enviesamento negativo, quando
    a média tem um valor menor do que a moda e a mediana.

    Quando os dados estão distribuidas com enviesamento, isso significa que talvez a amostragem não tenha sido feita corretamente.

    Executar as linhas abaixo no console python.
'''

from scipy.stats import skewnorm
from scipy import stats
import numpy as np
import seaborn as sns


def grafico_dados_normal():
    dados_normal = skewnorm.rvs(a=0, size=1000)
    media = dados_normal.mean()
    mediana = np.median(dados_normal).any()
    moda = stats.mode(dados_normal)[0][0]
    print("Média: %.2f, Mediana: %.2f, Moda: %.2f" %(media, mediana, moda))
    sns.distplot(dados_normal);


def grafico_dados_positivo():
    dados_positivo = skewnorm.rvs(a=10, size=1000)
    media = dados_positivo.mean()
    mediana = np.median(dados_positivo).any()
    moda = stats.mode(dados_positivo)[0][0]
    print("Média: %.2f, Mediana: %.2f, Moda: %s" %(media, mediana, moda))
    sns.distplot(dados_positivo);


def grafico_dados_negativo():
    dados_negativo = skewnorm.rvs(a=-10, size=1000)
    media = dados_negativo.mean()
    mediana = np.median(dados_negativo).any()
    moda = stats.mode(dados_negativo)[0][0]
    print("Média: %.2f, Mediana: %.2f, Moda: %s" %(media, mediana, moda))
    sns.distplot(dados_negativo);


grafico_dados_normal()
grafico_dados_positivo()
grafico_dados_negativo()