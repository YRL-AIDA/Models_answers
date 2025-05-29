import pandas as pd

df = pd.DataFrame({
    '': ['1', '2', '3', '4', '5', '6'],
    'Gene': ['serum response factor', 'enigma homolog', 'adrenomedullin', 'retinoblastoma inhibiting gene 1', 'CDC42 effector protein 3', 'adenosine A2b receptor'],
    'Locus Link': ['20807', '56376', '11535', '19649', '260409', '11541'],
    'Fold change': ['6.26', '4.75', '4.15', '3.92', '3.18', '2.56'],
    'Lower CI': ['4.66', '3.63', '3.28', '2.68', '2.40', '2.00'],
    'Upper CI': ['8.20', '6.28', '5.17', '5.75', '4.38', '3.24'],
    '% decrease in DN': ['59', '61', '57', '50', '48', '40'],
    'known SRE': ['YES', '', '', '', '', ''],
}, index=[0, 1, 2, 3, 4, 5])
