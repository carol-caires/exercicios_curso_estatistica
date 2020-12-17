import numpy as np
from scipy.stats import ttest_rel

base_H0 = np.array([149., 160., 147., 189., 175., 168., 156., 160., 152.])
base_H1 = base_H0 * 1.02

_, p = ttest_rel(a=base_H0, b=base_H1)

if p <= 0.01:
    print('hipótese nula rejeitada')
else:
    print('hipótese alternativa rejeitada')