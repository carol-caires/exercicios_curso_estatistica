from typing import TypedDict
from aleatoria_simples import AleatoriaSimples, globalDataset
from agrupamento import Agrupamento
from estratificada import Estratificada
from sistematica import Sistematica
from reservatorio import Reservatorio


class AgeDict(TypedDict):
    method: str
    mean: float


age_dict = []

as_ins = AleatoriaSimples()
as_ins.amostragem_aleatoria_simples(globalDataset, 1000)
item: AgeDict = {'method': 'Aleatória Simples', 'mean': as_ins.df_amostragem_aleatoria_simples['age'].mean()}
age_dict.append(item)

ag_ins = Agrupamento()
ag_ins.amostragem_agrupamento(globalDataset, 2)
item: AgeDict = {'method': 'Agrupamento', 'mean': ag_ins.df_amostragem_grupos['age'].mean()}
age_dict.append(item)

e_ins = Estratificada()
e_ins.amostragem_estratificada(globalDataset, 0.5)
item: AgeDict = {'method': 'Estratificada', 'mean': e_ins.df_amostragem_estratificada['age'].mean()}
age_dict.append(item)

asis_ins = Sistematica()
asis_ins.amostragem_sistematica(globalDataset, 1000)
item: AgeDict = {'method': 'Sistemática', 'mean': asis_ins.df_amostragem_sistematica['age'].mean()}
age_dict.append(item)

r_ins = Reservatorio()
r_ins.amostragem_reservatorio(globalDataset, 1000)
item: AgeDict = {'method': 'Reservatório', 'mean': r_ins.df_amostragem_reservatorio['age'].mean()}
age_dict.append(item)

dataset_mean = globalDataset['age'].mean()


def get_best_sampling_technique():
    best_diff: float = 9999
    best_technique_key = 0
    i = 0
    while i < len(age_dict):
        diff = abs(age_dict[i]['mean'] - dataset_mean)
        if diff < best_diff:
            best_diff = diff
            best_technique_key = i
        i += 1
    return age_dict[best_technique_key]


best_method = get_best_sampling_technique()
print("A melhor técnica de amostragem para esse dataset é a %s.\n"
      "Idade média do dataset: %.2f\n"
      "Idade média da amostragem: %.2f\n"
      % (best_method['method'], dataset_mean, best_method['mean']))
