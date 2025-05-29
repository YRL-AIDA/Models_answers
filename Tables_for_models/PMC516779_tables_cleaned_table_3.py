import pandas as pd

df = pd.DataFrame({
    '': ['anti-TPO+ vs anti-TPO-', 'Gender (F vs M)', 'Age (≤ 44 vs > 44)'],
    'p': ['0.001', '0.23', '0.08'],
    'OR': ['4.50', '1.58', '1.91'],
    'CI 95%': ['2.02 – 10.04', '0.75 – 3.31', '0.92 – 3.96'],
}, index=[0, 1, 2])
