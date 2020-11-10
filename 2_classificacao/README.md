## Exercício de Classificação

### Exercício do capítulo 2

O objetivo deste exercício é testar as técnicas de subamostragem e sobreamostragem utilizando outra base de dados

Carregue a base de dados csv_result-ebay_confianca_completo.csv, que é uma base de dados que utilizei no meu pós-doutorado para prever confiança de usuários baseado em traços de personalidade extraídos de textos

A classe é o atributo reputation, que pode ser reputação boa ou reputação ruim

Utilize o algoritmo Random Forest e faça os três testes conforme o exemplo anterior. O algoritmo Naïve Bayes não terá um bom desempenho nesta base de dados, por isso precisamos utilizar o Random Forest que é um algoritmo baseado em árvores de decisão. A ideia de utilização é a mesma, e no link a seguir você pode verificar a documentação: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html

### Como executar

1. A versão 0.5.0 da biblioteca imbalanced-learn deve ser usada. Se ocorrer qualquer erro
nas linhas de inicialização do TomekLinks ou do SMOTE, remover a versão atual da biblioteca e instalar novamente:

```
pip uninstall imbalanced-learn
pip install imbalanced-learn==0.5.0
```

2. 

```
make run-predictions
```

3. Se o script não se comportar como deveria, executar ``python reputacao_ebay.py`` que irá mostrar todos os possíveis warnings.