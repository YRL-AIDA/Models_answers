import pandas as pd

df = pd.DataFrame({
    'Diagnosis': ['', '', '', '', '', '', '', '', '', '', '', '', '', 'Date of the first diagnosis', 'Age at diagnosis', 'Sex', 'Residence', 'Language'],
    'Posterior and anterior uveal melanoma 1)': ['ICD10', 'C69.3 (Choroid)', 'C69.4 (Ciliary body)', 'ICD-O-3: Localisation', 'C69.42 (Iris)', 'C69.43 (Ciliary body +/- further choroid sections)', 'C69.3 (Choroid)', 'ICD-O-3 Histological types', '8720/3 (Malignant melamoma, NOS)', '8770/3 (Mixed epithelioid and spindle cell melanoma)', '8771/3 (Epithelioid cell melanoma)', '8773/3 (Spindle cell melanoma, type A)', '8774/3 (Spindle cell melanoma, type B)', '25.09.2002 – 24.09.2004 (24 months)', '20–74 years 2)', 'Man or woman', 'Germany', 'Being capable to complete the interview in German'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
