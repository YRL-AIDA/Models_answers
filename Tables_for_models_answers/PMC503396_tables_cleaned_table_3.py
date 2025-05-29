headers: (0,0);(0,1);(0,3);(1,1);(1,2);(1,3);(1,4)

import pandas as pd

df = pd.DataFrame({
    'Category': ['General pediatrics, non-academic', 'Academic general pediatrics', 'Academic non-pulmonary pediatric specialty', 'Academic pediatric pulmonology', 'Non-academic non-pulmonary pediatric specialty', 'Non-academic pediatric pulmonology', 'Non-pediatric medical specialty', 'Non-medical vocation', 'Unknown'],
    '+PF': ['1', '2', '1', '1', '3', '2', '1', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1'],
    '-PF': ['14.5*', '29', '5', '8.5', '12', '16', '0', '0', '1.5', '1.5', '0', '0', '0', '1', '0', '0', '2', '0'],
    '+PF': ['1', '2', '1', '1', '3', '2', '1', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1'],
    '-PF': ['14.5*', '29', '5', '8.5', '12', '16', '0', '0', '1.5', '1.5', '0', '0', '0', '1', '0', '0', '2', '0'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8])
