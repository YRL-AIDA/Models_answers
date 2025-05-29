import pandas as pd

df = pd.DataFrame({
    '': ['Exp.1', 'Exp.2', 'Mean value'],
    'untreated': ['76 ± 20 %', '96 ± 6 %', '86 %'],
    'H 2 O': ['69 ± 17 %', '98 ± 3 %', '83.5 %'],
    '10 μM BTH': ['37 ± 19 %', '39 ± 15 %', '38 %'],
    '50 μM BTH': ['18 ± 16 %', '7 ± 9 %', '12,5 %'],
}, index=[0, 1, 2])
