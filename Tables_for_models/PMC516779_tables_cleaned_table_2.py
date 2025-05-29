import pandas as pd

df = pd.DataFrame({
    '': ['anti-TPO+ vs anti-TPO-', 'Gender (F vs M)', 'Age (≤ 44 vs > 44)'],
    'p': ['0.01', '0.37', '0.71'],
    'OR': ['2.89', '1.38', '1.14'],
    'CI 95%': ['1.31–6.38', '0.68–2.82', '0.57–2.30'],
}, index=[0, 1, 2])
