import pandas as pd

df = pd.DataFrame({
    'Cell Type': ['Rat glial (C-6)', 'Human Colon Carcinoma (HT-29)', 'Human Breast Carcinoma (BT-20)'],
    'MEM/BSA control': ['9.0 ± 0.07', '7.8 ± 0.05', '12.1 ± 0.35'],
    'With epoxomicin': ['11.4 ± 0.28', '9.4 ± 0.33', '14.2 ± 0.31'],
}, index=[0, 1, 2])
