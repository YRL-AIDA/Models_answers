import pandas as pd

df = pd.DataFrame({
    'Transcriptome': ['Retinome', 'Heart (partial)', 'Liver (partial)', 'Prostate (partial)'],
    'No. of non-redundant genes identified in ≥ 2 studies a)': ['13,037', '3,660', '5,780', '7,018'],
    'Retina / RPE-specific genes b) (n = 43)': ['43', '0', '0', '0'],
    'Vitamin A / phototrans-duction pathway c) (n = 57)': ['53', '4', '7', '9'],
    'Retina / RPE genes (verified by immunohisto-chemistry d) ) (n = 260)': ['204', '59', '82', '92'],
    'Retinal disease genes e) (n = 102)': ['87', '18', '26', '28'],
    'Source / Reference': ['Present publication', 'UniGene Build 166, SAGE library GSM1499', 'UniGene Build 166, SAGE library GSM785', 'UniGene Build 166, SAGE libraries GSM685, GSM739, GSM764'],
}, index=[0, 1, 2, 3])
