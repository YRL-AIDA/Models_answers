import pandas as pd

df = pd.DataFrame({
    'Patient': ['B', 'A'],
    'Dose (mg)': ['100', '300'],
    'Age/sex': ['59 M', '75 M'],
    'Diagnosis': ['M5, de novo AML', 'M4, de novo AML'],
    'Stage': ['Relapse', 'New'],
    'Antigen expression': ['CD34+, CD33+', 'CD34+, CD33+'],
    'ras status': ['WT', 'WT'],
}, index=[0, 1])
