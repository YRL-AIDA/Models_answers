import pandas as pd

df = pd.DataFrame({
    '': ['Baseline weight', 'Number of diets in past year', 'Weight outcome evaluations 1', 'Self-motivation', 'Body size dissatisfaction'],
    'B': ['-.069', '.372', '.235', '-.040', '.755'],
    't': ['-2.481', '2.439', '3.673', '-2.714', '2.389'],
    'p': ['0.015', '0.016', '<0.001', '0.008', '0.018'],
    'Squared semi-partial correlation (%)': ['4.0', '3.8', '8.7', '4.7', '3.7'],
}, index=[0, 1, 2, 3, 4])
