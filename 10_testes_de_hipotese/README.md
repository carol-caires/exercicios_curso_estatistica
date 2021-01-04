# Teste de Hipótese

Para verificar se há diferença estatística entre dois ou mais conjuntos de dados, podemos usar os testes 
ANOVA e Tukey para dados normais e Kruskal-Wallis e Nemenyi para dados que não temos certeza se são normais ou não.

O ANOVA e o Kruskal-Wallis rejeitam a hipótese nula se há diferença em pelo menos 2 dos grupos comparados, mas não
nos diz quais são esses grupos. Para verificar quais são esses grupos, usar os testes de Tukey e Nemenyi, pois eles fazem
comparações multiplas.

Aqui explica melhor a diferenças desses testes: https://operdata.com.br/blog/teste-de-kruskal-wallis-e-o-teste-de-nemenyi/

## Exercício

Assim como você pode fazer testes de hipóteses usando a estatística Z, é também possível utilizar a estatística T da Distribuição T Student para realizar testes de hipóteses quando você possui poucos registros (até 30 amostras). Implemente a base de dados abaixo com a alturas de somente 9 pessoas

```
np.array([149. , 160., 147., 189., 175., 168., 156., 160., 152.])
```

Depois siga o seguinte roteiro:

- Crie uma nova variável também com alturas de 9 pessoas, porém, com valores diferentes

- Faça a importação do pacote from scipy.stats import ttest_rel para realizar o teste de hipótese. Caso tenha dúvidas, consulte aqui a documentação

- Realize o teste de hipótese para verificar se as distribuições são ou não são diferentes

## Exercício 2

Nas aulas anteriores nós fizemos os testes de hipóteses utilizando técnicas de estatística não paramétrica. Porém, como os resultados dos algoritmos seguem uma distribuição normal (conforme os testes de normalidade realizados), o objetivo desta tarefa é aplicar o ANOVA e também o teste de Tukey para comparar os resultados dos algoritmos