import pandas as pd

df = pd.DataFrame({
    'Chemical': ['BaP', 'BaP/ANTH', 'Chemical', 'BaP', 'BaP/CHRY'],
    'Con (μM)': ['30', '30/3', 'Con (μM)', '30', '30/3'],
    'Calc. BaP (μM)': ['14.39 ± 0.18', '13.72 ± 1.41', 'Calc. BaP (μM)', '17.3 ± 0.29', '17.4 ± 1.2'],
    'Calc. ANTH (μM)': ['_', '3.7 ± 0.49', 'Calc. CHRY (μM)', '_', '2.31 ± 0.12'],
    'BaP 3(OH) (μM)': ['0.026 ± 0.0', '0.005 ± 0.003', 'BaP 3(OH) (μM)', '0.013 ± 0.002', '0.007 ± 0.002'],
}, index=[0, 1, 2, 3, 4])
