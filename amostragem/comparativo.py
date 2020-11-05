from aleatoria_simples import AleatoriaSimples, globalDataset
from agrupamento import Agrupamento
from estratificada import Estratificada
from sistematica import Sistematica
from reservatorio import Reservatorio

# as_ins = AleatoriaSimples()
# as_ins.amostragem_aleatoria_simples(globalDataset, 1000)
# print(as_ins.df_amostragem_aleatoria_simples.shape)
# print(as_ins.df_amostragem_aleatoria_simples.head())
#
# ag_ins = Agrupamento()
# ag_ins.amostragem_agrupamento(globalDataset, 2)
# print(ag_ins.df_amostragem_grupos.shape)
# print(ag_ins.df_amostragem_grupos.head())

# e_ins = Estratificada()
# e_ins.amostragem_estratificada(globalDataset, 0.5)
# print(e_ins.df_amostragem_estratificada.shape)
# print(e_ins.df_amostragem_estratificada.head())
# print(e_ins.df_amostragem_estratificada['c#default'].value_counts())

# asis_ins = Sistematica()
# asis_ins.amostragem_sistematica(globalDataset, 1000)
# print(asis_ins.df_amostragem_sistematica.shape)
# print(asis_ins.df_amostragem_sistematica.head())

# r_ins = Reservatorio()
# r_ins.amostragem_reservatorio(globalDataset, 1000)
# print(r_ins.df_amostragem_reservatorio.shape)
# print(r_ins.df_amostragem_reservatorio.head())

# print("Idade média dos candidatos:", globalDataset['age'].mean())
# print("Idade média dos candidatos (amostragem aleatória simples):", as_ins.df_amostragem_aleatoria_simples['age'].mean())