headers: (0,0);(0,1);(0,2);(0,3);(0,4)

import pandas as pd

df = pd.DataFrame({
    'NCI CTC Grade': ['Leukopenia', 'Neutropenia', 'Anaemia'],
    '1': ['7', '4', '3'],
    '2': ['1', '7', '1'],
    '3': ['0', '3', '0'],
    '4': ['1', '0', '0'],
}, index=[0, 1, 2])
