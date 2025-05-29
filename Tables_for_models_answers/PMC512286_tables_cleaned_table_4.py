headers: (0,0);(0,1);(0,2)

import pandas as pd

df = pd.DataFrame({
    'Source of Variation': ['Health-category by Age-category', 'Health-category by Gender', 'Age-category by gender'],
    'F-value': ['0.65', '0.20', '0.40'],
    'P-value': ['0.833', '0.937', '0.807'],
}, index=[0, 1, 2])
