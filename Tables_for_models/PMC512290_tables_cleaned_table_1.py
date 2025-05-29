import pandas as pd

df = pd.DataFrame({
    'Grade of tumor invasion': ['1 (1 + 2)', '2 (3)', '3 (4a + 4b)', 'Total'],
    'Negative/weak (0 + 1)': ['15 (83.3%)', '14 (32.6%)', '5 (29.4%)', '34'],
    'Moderate/ extensive (2 + 3)': ['3 (16.7%)', '29 (67.4%)', '12 (70.6%)', '44'],
    'Total': ['18', '43', '17', '78'],
}, index=[0, 1, 2, 3])
