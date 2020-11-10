from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from imblearn.under_sampling import TomekLinks
from imblearn.over_sampling import SMOTE
import pandas as pd


class Classificacao:
    @staticmethod
    def predict(dataset):
        # converte a coluna blacklist do dataset para converter de texto para booleano
        dataset["blacklist"] = dataset["blacklist"] == 'S'

        X = dataset.iloc[:, 0:74].values  # colunas que serão usadas como base da predição
        y = dataset.iloc[:, 74].values  # coluna de reputação (a ser predita)

        X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, y, test_size=0.2, stratify=y)
        score = Classificacao.__get_score(X_treinamento, y_treinamento, X_teste, y_teste)
        score_o = Classificacao.__oversampling(X, y)
        score_u = Classificacao.__undersampling(X, y)
        return {'score': score, 'score_oversampling': score_o, 'score_undersampling': score_u}

    @staticmethod
    def __oversampling(X, y):
        smote = SMOTE(ratio='minority')
        X_over, y_over = smote.fit_sample(X, y)
        X_treinamento_o, X_teste_o, y_treinamento_o, y_teste_o = train_test_split(X_over, y_over, test_size=0.2,
                                                                                  stratify=y_over)
        return Classificacao.__get_score(X_treinamento_o, y_treinamento_o, X_teste_o, y_teste_o)

    @staticmethod
    def __undersampling(X, y):
        tl = TomekLinks(return_indices=True, ratio='majority')
        X_under, y_under, id_under = tl.fit_sample(X, y)
        X_treinamento_u, X_teste_u, y_treinamento_u, y_teste_u = train_test_split(X_under, y_under, test_size=0.2,
                                                                                  stratify=y_under)
        return Classificacao.__get_score(X_treinamento_u, y_treinamento_u, X_teste_u, y_teste_u)

    @staticmethod
    def __get_score(X_treinamento, y_treinamento, X_teste, y_teste):
        modelo = RandomForestClassifier()
        modelo.fit(X_treinamento, y_treinamento)
        previsoes = modelo.predict(X_teste)
        return accuracy_score(previsoes, y_teste)


dataset = pd.read_csv('csv_result-ebay_confianca_completo.csv')
scores = Classificacao.predict(dataset)
print(scores)
