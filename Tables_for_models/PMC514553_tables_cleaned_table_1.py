import pandas as pd

df = pd.DataFrame({
    'Type of vignette': ['Depression', 'Pre-test', 'Follow-up', 'Change (95% CI)', 'Schizophrenia', 'Pre-test', 'Follow-up', 'Change (95% CI)', 'Both vignettes', 'Pre-test', 'Follow-up', 'Change (95% CI)'],
    'MHFA group': ['', '90.2%', '95.8%', '5.6% (0.5 to 10.7)', '', '74.6%', '82.6%', '8.0% (1.5 to 14.4)', '', '70.6%', '80.2%', '9.6% (2.8 to 16.4)'],
    'Control group': ['', '87.7%', '90.3%', '2.6% (-2.8 to 8.0)', '', '83.9%', '81.9%', '-2.0% (-6.8 to 2.8)', '', '76.5%', '77.8%', '1.3% (-5.2 to 7.9)'],
    'P-value for group × time interaction': ['.091', '', '', '', '.083', '', '', '', '.189', '', '', ''],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
