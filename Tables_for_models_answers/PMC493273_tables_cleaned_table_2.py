headers: (0,0);(0,1);(1,1);(1,2);(1,3)

import pandas as pd

df = pd.DataFrame({
    'Drug & dose (mg)': ['Rofecoxib 25', 'Rofecoxib 50', 'Ibuprofen 400', 'Naproxen sodium 550', 'Placebo'],
    '6': ['21', '22', '22', '18', '37'],
    '8': ['25', '24', '35', '24', '44'],
    '12': ['28', '27', '41', '29', '50'],
}, index=[0, 1, 2, 3, 4])
