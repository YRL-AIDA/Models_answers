headers: (0,0);(0,1);(0,2);(0,3)

import pandas as pd

df = pd.DataFrame({
    'Mental health problems in:': ['Self', 'Pre-test', 'Follow-up', 'Change (95% CI)', 'Family', 'Pre-test', 'Follow-up', 'Change (95% CI)'],
    'MHFA group': ['', '60.0%', '65.5%', '5.5% (0.5 to 10.6)', '', '74.5%', '77.2%', '2.8% (-3.9 to 9.4)'],
    'Control group': ['', '49.7%', '55.6%', '5.9% (0.6 to 11.1)', '', '73.0%', '75.7%', '2.6% (-3.5 to 8.7)'],
    'P-value for group × time interaction': ['.577', '', '', '', '.849', '', '', ''],
}, index=[0, 1, 2, 3, 4, 5, 6, 7])
