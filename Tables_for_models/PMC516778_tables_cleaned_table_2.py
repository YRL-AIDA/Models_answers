import pandas as pd

df = pd.DataFrame({
    'Trauma type': ['Unwanted sex', 'Physical assault', 'Sudden violent death', 'Sudden unexpected death of loved one', 'Sexual assault', 'Fire/explosion', 'Weapon assault', 'Combat', 'Life-threatening illness', 'Other'],
    'Number of patients, N = 33': ['11', '6', '4', '3', '2', '1', '1', '1', '1', '3'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
