import pandas as pd

df = pd.DataFrame({
    '': ['17β-estradiol (pg/ml)', 'Progesterone (ng/ml)'],
    'Pre-treatment baseline levels': ['626 ± 91', '0.58 ± 0.14'],
    '700 mg/d dose': ['164 ± 30', '8.4 ± 2.6'],
    'P -value': ['0.04', '0.10'],
    '1.4 g/d dose': ['92.5 ± 3.5', '16.8 ± 0.7'],
    'P-value': ['0.03', '0.002'],
}, index=[0, 1])
