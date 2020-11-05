from aleatoria_simples import AleatoriaSimples, globalDataset
from agrupamento import Agrupamento
from estratificada import Estratificada
from sistematica import Sistematica
from reservatorio import Reservatorio

as_ins = AleatoriaSimples()
as_ins.amostragem_aleatoria_simples(globalDataset, 1000)

ag_ins = Agrupamento()
ag_ins.amostragem_agrupamento(globalDataset, 2)

e_ins = Estratificada()
e_ins.amostragem_estratificada(globalDataset, 0.5)

asis_ins = Sistematica()
asis_ins.amostragem_sistematica(globalDataset, 1000)

r_ins = Reservatorio()
r_ins.amostragem_reservatorio(globalDataset, 1000)

print("Médias de Idade:")
print("dataset:", globalDataset['age'].mean())
print("amostragem aleatória simples:", as_ins.df_amostragem_aleatoria_simples['age'].mean())
print("amostragem de grupos:", ag_ins.df_amostragem_grupos['age'].mean())
print("amostragem estratificada:", e_ins.df_amostragem_estratificada['age'].mean())
print("amostragem sistemática:", asis_ins.df_amostragem_sistematica['age'].mean())
print("amostragem de reservatório:", r_ins.df_amostragem_reservatorio['age'].mean())

print("Melhor forma de amostragem para esse dataset:")

# todo: analisar e colocar a resposta
