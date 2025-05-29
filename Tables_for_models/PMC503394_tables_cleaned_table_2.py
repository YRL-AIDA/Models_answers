import pandas as pd

df = pd.DataFrame({
    'Characteristic': ['Location (Boston)', 'Age (< 65)', 'Women', 'White', 'Attended some college', 'At least 5 years since first back pain lasting longer than 2 weeks', '90+ days of LBP in last 6 mo.', 'High symptom bothersomeness in the past week (≥ 7) on 0 – 10 scale', 'Used medication for LBP in the past week', 'Expect pain to be similar in a year'],
    'Percent': ['43', '52', '60', '80', '57', '60', '61', '42', '56', '72'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
