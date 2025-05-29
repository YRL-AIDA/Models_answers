headers: (0,0);(0,1);(1,1);(1,2);(1,3)

import pandas as pd

df = pd.DataFrame({
    '': ['Triglycerides (mM/l) †', 'HDL Cholesterol (mM/l) ‡', 'Non-HDL cholesterol (mM/l) ‡', 'Cholesterol (mM/l) ‡', 'LDL Cholesterol (mM/l) ‡'],
    'Baseline': ['3.01 ± 0.7', '0.91 ± 0.1', '4.57 ± 0.9', '5.5 ± 0.9', '3.1 ± 0.9'],
    'Final': ['1.61 ± 0.8', '0.98 ± 0.4', '3.61 ± 1.5', '4.57 ± 1.8', '2.8 ± 1.3'],
    'Percent change': ['-44 ± 33*', '10 ± 52*', '-19 ± 36*', '-14.9 ± 35*', '-5.4 ± 59*'],
}, index=[0, 1, 2, 3, 4])
