headers: (0,0);(0,1);(0,3);(1,1);(1,2)

import pandas as pd

df = pd.DataFrame({
    'Intervention': ['Thrombolytic therapy*', 'β blocker on discharge*', 'Aspirin*', 'ACE inhibitors', 'Exercise testing', 'Coronary angiography', 'Coronary angioplasty', 'Coronary artery bypass grafting'],
    'Cardiologist (275)': ['140 (51%)', '206 (75%)', '264 (96%)', '124 (45%)', '192 (70%)', '151 (55%)', '74 (27%)', '66 (24%)'],
    'Non Cardiologist (201)': ['66 (33%)', '90 (45%)', '160 (80%)', '80 (40%)', '46 (23%)', '12 (6%)', '30 (15%)', '30 (15%)'],
    'Odds ratio (95% CI)': ['2.08 (1.35 – 3.23)', '3.70 (2.38 – 5.56)', '6.67 (3.23 – 14.29)', '1.27 (0.01 – 1.92)', '7.70 (4.76 – 12.50)', '4.76 (3.22 – 7.14)', '1.92 (1.28 – 2.94)', '1.75 (1.15 – 2.70)'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7])
