## Exercício de Classificação

### Exercício do capítulo 2

O objetivo deste exercício é testar as técnicas de subamostragem e sobreamostragem utilizando outra base de dados

Carregue a base de dados csv_result-ebay_confianca_completo.csv, que é uma base de dados que utilizei no meu pós-doutorado para prever confiança de usuários baseado em traços de personalidade extraídos de textos

A classe é o atributo reputation, que pode ser reputação boa ou reputação ruim

Utilize o algoritmo Random Forest e faça os três testes conforme o exemplo anterior. O algoritmo Naïve Bayes não terá um bom desempenho nesta base de dados, por isso precisamos utilizar o Random Forest que é um algoritmo baseado em árvores de decisão. A ideia de utilização é a mesma, e no link a seguir você pode verificar a documentação: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html