headers: (0,0);(0,1);(0,2);(0,3)

import pandas as pd

df = pd.DataFrame({
    '': ['Dead before discharge*', 'Birthweight (g)', '<= 750', '751–1000', '1001–1250', 'Apgar Score < 6 at 5 minutes', 'Oxygen (days)', '0–10', '11–27', '>= 28', 'Sepsis', 'Peri–intraventricular hemorrhage > grade III', 'Necrotizing Enterocolitis >= II degree'],
    'Historic controls Year 1999 – 2000 N = 35† n(%)': ['18 (34.0)', '', '4 (11.4)', '13 (37.1)', '18 (51.4)', '10 (28.6)', '', '9 (25.7)', '10 (28.6)', '16 (45.7)', '16 (45.7)', '8 (22.9)', '5 (14.3)'],
    'Ketorolac Year 2001–2002 N = 43† n(%)': ['16 (27.1)', '', '8 (18.6)', '9 (20.9)', '26 (60.59', '11 (25.5)', '', '21 (48.8)', '15 (34.9)', '7 (16.3)', '24 (55.8)', '6 (14.0)', '9 (20.9)'],
    'p**': ['0.54', '0.28', '', '', '', '0.80', '0.01', '', '', '', '0.50', '0.38', '0.56'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
