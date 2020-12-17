# Teste de Hipótese

## Exercício

Assim como você pode fazer testes de hipóteses usando a estatística Z, é também possível utilizar a estatística T da Distribuição T Student para realizar testes de hipóteses quando você possui poucos registros (até 30 amostras). Implemente a base de dados abaixo com a alturas de somente 9 pessoas

```
np.array([149. , 160., 147., 189., 175., 168., 156., 160., 152.])
```

Depois siga o seguinte roteiro:

- Crie uma nova variável também com alturas de 9 pessoas, porém, com valores diferentes

- Faça a importação do pacote from scipy.stats import ttest_rel para realizar o teste de hipótese. Caso tenha dúvidas, consulte aqui a documentação

- Realize o teste de hipótese para verificar se as distribuições são ou não são diferentes