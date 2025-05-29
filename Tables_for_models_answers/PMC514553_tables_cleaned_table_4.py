headers: (0,0);(0,1);(0,2);(0,3)

import pandas as pd

df = pd.DataFrame({
    'Scale': ['Mental health', 'Pre-test mean (SD)', 'Follow-up mean (SD)', 'Change (95% CI)', 'Physical health', 'Pre-test mean (SD)', 'Follow-up mean (SD)', 'Change (95% CI)'],
    'MHFA group': ['', '45.43 (11.40)', '47.48 (11.11)', '2.06 (0.39 to 3.72)', '', '51.38 (7.97)', '50.74 (8.14)', '-0.64 (-1.80 to 0.53)'],
    'Control group': ['', '45.40 (10.17)', '45.11 (11.25)', '-0.29 (-1.72 to 1.14)', '', '51.97 (8.11)', '51.90 (8.68)', '-0.07 (-1.29 to 1.16)'],
    'P-value for group × time interaction': ['.035', '', '', '', '.506', '', '', ''],
}, index=[0, 1, 2, 3, 4, 5, 6, 7])
