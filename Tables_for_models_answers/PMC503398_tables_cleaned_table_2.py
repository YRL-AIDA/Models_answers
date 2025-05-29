headers: (0,0);(0,1);(0,2)

import pandas as pd

df = pd.DataFrame({
    'Variable': ['Constant', 'BMI < 25 kg/m 2', 'Mixed hyperlipidemia', 'Percent of change of triglycerides'],
    'Beta coefficient ± standard error': ['14.4 ± 2.6', '7.6 ± 3.6', '0.82 ± 0.2', '0.68 ± 0.4'],
    'p value': ['< 0.001', '0.036', '0.003', '< 0.001'],
}, index=[0, 1, 2, 3])
