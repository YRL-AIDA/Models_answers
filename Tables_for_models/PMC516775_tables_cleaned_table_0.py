import pandas as pd

df = pd.DataFrame({
    '': ['Exp.1', 'Exp.2', 'Mean value'],
    'untreated': ['66 ± 24 %', '68 ± 28 %', '67 %'],
    'H 2 O': ['57 ± 25 %', '71 ± 23 %', '64 %'],
    '10 μM BTH': ['12 ± 9 %', '34 ± 30 %', '23 %'],
    '50 μM BTH': ['13 ± 11 %', '5 ± 6 %', '9 %'],
}, index=[0, 1, 2])
