headers: (0,0);(0,1);(0,2)

import pandas as pd

df = pd.DataFrame({
    '': ['Median (range)', 'Missing values', 'Male', 'Female', 'Missing values', '< 10 years', '10–12 years', '> 12 years', 'Missing values', '1 (highest level)', '2', '3', '4', '5 (lowest level)', 'Missing values', 'University of Hamburg', 'Vocational College', 'Non-academic students'],
    'Frequency tree (n = 94)': ['29 (20–54)', '3 (3)', '15 (16)', '77 (82)', '2 (3)', '1 (1)', '22 (23)', '68 (72)', '3 (3)', '6 (6)', '20 (21)', '35 (37)', '14 (15)', '5 (5)', '14 (15)', '59 (63)', '14 (15)', '21 (22)'],
    '2 × 2 table (n = 90)': ['26 (19–51)', '2 (2)', '20 (22)', '67 (75)', '3 (3)', '1 (1)', '19 (21)', '67 (75)', '3 (3)', '6 (7)', '18 (20)', '32 (36)', '17 (19)', '9 (10)', '8 (9)', '55 (61)', '15 (17)', '20 (22)'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
