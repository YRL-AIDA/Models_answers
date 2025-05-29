import pandas as pd

df = pd.DataFrame({
    '': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
    'Gene': ['similar to Hs Mitogen inducible gene 6', 'coagulation factor III', 'retinoblastoma inhibiting gene 1', 'tropomyosin 1, alpha', 'pleckstrin homology-like domain', 'epiregulin', 'leukemia inhibitory factor', 'serum response factor', 'tribbles homolog 1', 'aortic alpha actin-2', 'fos-like antigen 1', 'CDC42 effector protein 3'],
    'Locus Link': ['74155', '14066', '19649', '22003', '21664', '13874', '16878', '20807', '211770', '68377', '14283', '260409'],
    'Fold change': ['18.67', '8.05', '6.45', '5.92', '5.82', '5.77', '4.84', '4.7', '3.87', '3.77', '3.02', '2.47'],
    'Lower CI': ['12.81', '5.44', '4.97', '4.18', '3.67', '3.15', '2.79', '3.25', '2.81', '2.94', '2.27', '2.19'],
    'Upper CI': ['26.3', '14.29', '8.90', '8.55', '11.48', '9.27', '7.65', '6.40', '5.10', '5.06', '3.89', '2.81'],
    '% decrease in DN': ['54', '47', '63', '63', '65', '71', '57', '60', '50', '52', '44', '46'],
    'known SRE': ['', '', '', 'YES', '', '', '', 'YES', '', 'YES', 'YES', ''],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
