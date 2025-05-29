import pandas as pd

df = pd.DataFrame({
    'Gene': ['TLR1', 'TLR2', 'TLR3', 'TLR4', 'TLR5', 'TLR6', 'TLR7', 'TLR8', 'TLR9', 'TLR10', 'GAPDH'],
    'Fold change TNFα stimulated': ['ND', '0.6', '1.6', '3.5', '0.9', '0.9', 'M', 'ND', '0.2', '0.3', '1.0'],
    'Fold change FliC stimulated': ['ND', '1.3', '0.6', '1.1', '0.5', '0.6', 'M', 'ND', '0.5', '0.5', '1.0'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
