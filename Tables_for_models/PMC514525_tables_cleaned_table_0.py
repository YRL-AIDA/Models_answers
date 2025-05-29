import pandas as pd

df = pd.DataFrame({
    '': ['n', 'Identified on CT', 'Identified on US', 'Hydrouretero-nephrosis on CT', 'Hydrouretero-nephrosis on US'],
    'Upper ureter': ['6', '6', '4', '6', '4'],
    'Middle ureter': ['14', '14', '5', '14', '8'],
    'Distal ureter': ['2', '2', '1', '2', '1'],
}, index=[0, 1, 2, 3, 4])
