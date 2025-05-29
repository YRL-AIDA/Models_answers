import pandas as pd

df = pd.DataFrame({
    '': ['Correlation', 'Naive (p < 0.05)', 'Bonferroni', 'FDR 10%'],
    'Between strains MA-ANOVA': ['', '718', '0', '88'],
    'CBA': ['0.95', '737', '2', '2'],
    'BL10': ['0.95', '610', '4', '4'],
    'BL6': ['0.87', '963', '1', '14'],
    'DBA': ['0.87', '1043', '0', '0'],
    'BALB': ['0.92', '483', '3', '16'],
}, index=[0, 1, 2, 3])
