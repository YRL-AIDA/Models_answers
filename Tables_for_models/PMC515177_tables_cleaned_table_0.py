import pandas as pd

df = pd.DataFrame({
    'Clinical category': ['MR/SCZ', 'MR/BP1', 'MR/SCAFF', 'MR/UFP', 'MR/UPR', 'TOTAL SCREEN'],
    'MAPH alone': ['34', '6', '1', '3', '1', '45'],
    'MAPH and FISH': ['7', '3', '2', '0', '0', '12'],
    'FISH alone': ['8', '2', '0', '2', '0', '12'],
}, index=[0, 1, 2, 3, 4, 5])
