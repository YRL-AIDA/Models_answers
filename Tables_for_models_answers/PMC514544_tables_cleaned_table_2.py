headers: (0,0);(0,1);(0,2);(0,3);(0,4)

import pandas as pd

df = pd.DataFrame({
    'Symptoms': ['Pre-symptoms', 'Pains in the chest', 'Dizziness', 'Syncope', 'Breathlessness when resting', 'Breathlessness when working', 'Swollen ankles', 'Palpitation at rest', 'Palpitation at exercise', 'Nausea', 'Vomiting', 'Abdominal pain', 'Loss of appetite', 'Anxiety', 'Reduced physical capacity', 'Polyuria*'],
    'Total n = 100': ['32', '25', '52', '7', '41', '70', '10', '86', '88', '19', '2', '5', '31', '59', '87', '40/75'],
    'Males n = 72': ['20 (28%)', '14 (19%)', '33 (46%)', '4 (6%)', '32 (44%)', '53 (74%)', '4 (6%)', '62 (86%)', '59 (82%)', '9 (13%)', '1 (1%)', '2 (3%)', '20 (28%)', '37 (51%)', '62 (86%)', '25/52 (48%)'],
    'Female n = 28': ['12 (43%)', '11 (39%)', '19 (68%)', '3 (11%)', '9 (32%)', '17 (61%)', '6 (21%)', '24 (86%)', '23 (82%)', '10 (36%)', '1 (4%)', '3 (11%)', '11 (39%)', '22 (79%)', '25 (89%)', '15/23 (65%)'],
    'p-value': ['0.159', '0.070', '0.074', '0.396', '0.365', '0.230', '0.027', '>0.999', '>0.999', '0.012', '0.484', '0.312', '0.336', '0.014', '>0.999', '0.213'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
