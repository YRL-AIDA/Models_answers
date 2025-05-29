import pandas as pd

df = pd.DataFrame({
    'Medication type': ['SSRIs', 'Benzodiazepines', 'Stimulants', 'Atypical neuroleptics', 'Gabapentin', 'Lamotrigine', 'Mirtazapine', 'Venlafaxine', 'Verapamil', 'Other', 'Monotherapy'],
    'Number of patients (N = 33)': ['12', '10', '6', '3', '3', '5', '3', '3', '1', '8', '5'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
