headers: (0,0);(0,1);(0,2);(0,3);(0,4);(0,5);(0,6)

import pandas as pd

df = pd.DataFrame({
    'Subject': ['1', '2', '3'],
    'Pretreatment menstrual cycling history obtained': ['Cycles 1–3', 'Cycles 1–3', 'Cycles 1–3'],
    'Pretreatment serum 17β-estradiol and progesterone levels ascertained (Cycle and day)': ['Cycle 2, day 12; Cycle 3, day 12', 'NA', 'NA'],
    'Treatment period/dose': ['Cycle 4–5/ 700 mg/d', 'Cycle 6–7/ 1.4 g/d', 'Cycle 4–5/ 700 mg/d', 'NA', 'Cycle 4–5/ 700 mg/d', 'Cycle 6–7/ 1.4 g/d'],
    'Treatment serum 17β-estradiol and progesterone levels ascertained (Cycle and day)': ['Cycle 4, day 12; Cycle 4, day 21; Cycle 5, day 21', 'Cycle 6, day 21; Cycle 7, day 21', 'NA', 'NA', 'NA', 'NA'],
    'Treatment period/dose': ['Cycle 4–5/ 700 mg/d', 'Cycle 6–7/ 1.4 g/d', 'Cycle 4–5/ 700 mg/d', 'NA', 'Cycle 4–5/ 700 mg/d', 'Cycle 6–7/ 1.4 g/d'],
    'Treatment serum 17β-estradiol and progesterone levels ascertained (Cycle and day)': ['Cycle 4, day 12; Cycle 4, day 21; Cycle 5, day 21', 'Cycle 6, day 21; Cycle 7, day 21', 'NA', 'NA', 'NA', 'NA'],
}, index=[0, 1, 2])
