import pandas as pd

df = pd.DataFrame({
    'Grade of tumor invasion': ['1 (1 + 2)', '2 (3)', '3 (4a + 4b)', 'Total'],
    'Negative/weak (0 + 1)': ['13 (72.2%)', '16 (37.2%)', '7 (41.2%)', '36'],
    'Moderate/ extensive (2 + 3)': ['5 (27.8%)', '27 (62.8%)', '10 (58.8%)', '42'],
    'Total': ['18', '43', '17', '78'],
}, index=[0, 1, 2, 3])
