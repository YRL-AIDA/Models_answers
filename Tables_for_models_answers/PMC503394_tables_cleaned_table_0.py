headers: (0,0);(0,1);(1,1);(1,2);(1,3);(1,4);(1,5);(1,6)

import pandas as pd

df = pd.DataFrame({
    'Potential Predictor Variable': ['Geographic location (Boston vs. Seattle)', 'Age (65+ vs. < 65)', 'Gender (female vs. male)', 'Race (white, non-white)', 'Education (no college vs. some college)', '≥ 5 years since first back pain', '≥ 90 days of LBP in last 6 mo.', 'High symptom bothersomeness (7 – 10) on a 0 – 10 scale', 'High knowledge of therapy (4 or 5) on a 1 – 5 scale', 'Prior use of therapy', 'Prior use of therapy for back pain', 'High expectations of therapy (7 – 10) on a 0 – 10 scale', 'Medication usage in past week', 'Prior harm from therapy'],
    'High Knowledge of Therapy*': ['X ¶', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '', '', '', '', '', ''],
    'Prior Use of Therapy*': ['X', 'X', 'X', 'X', 'X', '', '', '', '', '', '', '', '', ''],
    'Prior Use of Therapy for Back Pain*': ['X', 'X', 'X', 'X', 'X', '', '', '', '', '', '', '', '', ''],
    'High Expectations of Success of Therapy*': ['X', 'X', 'X', 'X', 'X', '', '', '', 'X', 'X', 'X', '', '', ''],
    'Likelihood of Trying Therapy at No Cost*': ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    'Likelihood of Trying Therapy for $10 Co-pay**': ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
