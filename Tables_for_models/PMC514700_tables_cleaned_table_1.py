import pandas as pd

df = pd.DataFrame({
    '': ['True positive', 'False positive', 'False negative', 'Sensitivity %', 'Specificity %'],
    'Criteria 1': ['4339', '987', '110', '97.5', '81.5'],
    'Criteria 2': ['4305', '602', '144', '96.8', '87.7'],
    'Criteria 3': ['4303', '555', '146', '96.7', '88.6'],
}, index=[0, 1, 2, 3, 4])
