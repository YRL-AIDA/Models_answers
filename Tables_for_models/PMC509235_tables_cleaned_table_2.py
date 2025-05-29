import pandas as pd

df = pd.DataFrame({
    'Gene': ['E1', 'E6', 'E7', 'L1'],
    "Mantel's Correlation Coefficient": ['0.97', '0.92', '0.88', '0.96'],
    'Partition Metric': ['12', '10', '14', '12'],
}, index=[0, 1, 2, 3])
