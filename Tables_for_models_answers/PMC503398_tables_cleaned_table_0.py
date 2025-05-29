headers: (0,0);(0,1)

import pandas as pd

df = pd.DataFrame({
    'Variable': ['Male (n(%))', 'Female (n(%))', 'Age (years)*', 'Body mass index (kg/m 2 )', 'Diabetes (n(%))', 'Fasting plasma glucose (mM/l)*', 'Family history of dyslipidemia (n(%))', 'Coronary heart disease (n(%))', 'Aspartate aminotranferase (mU/l)', 'Alanine aminotransferase (mU/l)'],
    'N = 437': ['239 (54.7)', '198 (45.3)', '54.7 ± 12.1', '28.8 ± 4.6', '125 (28.7)', '5.2 ± 0.6', '171 (39.2)', '196 (45)', '23 ± 11', '26 ± 14'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
