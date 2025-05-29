headers: (0,0);(0,1);(0,3);(1,1);(1,2);(1,3);(1,4)

import pandas as pd

df = pd.DataFrame({
    'Category': ['0–1 (0–1 answer correct)', '2–3 (2–3 answers correct)', '4–5 (4–5 answers correct)'],
    'Frequency tree (n = 94)': ['19(20)', '20 (21)', '55 (59)'],
    '2 × 2 table (n = 90)': ['18(20)', '20 (22)', '52(58)'],
    'Frequency tree (n = 74)': ['53 (72)', '2 (3)', '19 (26)'],
    '2 × 2 table (n = 75)': ['50 (67)', '5 (7)', '20(27)'],
}, index=[0, 1, 2])
