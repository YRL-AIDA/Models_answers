headers: (0,0);(0,1);(1,1);(1,2);(1,3);(1,4);(1,5)

import pandas as pd

df = pd.DataFrame({
    'Dependent Variable': ['High Knowledge of specific therapy (4–5)', '', 'Previously tried specific therapy', 'Previously tried specific therapy for back pain', 'High expectations of specific therapy (7 – 10)', '', 'Very likely to try specific therapy for free', '', 'Very likely to try specific therapy for $10 /visit co-pay', ''],
    'Acupuncture': ['Tried acupuncture: 43.6 (16.7–113.6)', '', 'No associations', 'No associations', '65+ yrs: 0.4(0.2 – 0.8)', 'Tried acupuncture: 4.3 (2.1 – 9.0)', 'High expectations: 15.4 (3.6 – 66.1)', '', 'High expectations: 6.8 (3.0 – 15.5)', 'Bostonian: 2.3 (1.4 – 4.0)'],
    'Chiropractic': ['Tried chiropractic: 12.8 (6.2–26.7)', '', 'Bostonian: 0.5 (0.3 – 0.8)', 'None', 'Knowledge: 2.9 (1.6 – 5.2)', '', 'High expectations: 27.4 (9.5 – 79.3)', '', 'High expectations: 8.1 (4.2 – 15.7)', ''],
    'Massage': ['Tried massage: 7.6 (4.0 – 14.7)', '', '65+ yrs: 0.4 (0.2 – 0.7)', '65+ yrs: 0.3 (0.2 – 0.6)', '65+ yrs: 0.3 (0.2 – 0.5)', '', 'High expectations: 16.4 (7.4 – 36.5)', '', 'High expectations: 6.4 (3.5 – 11.4)', 'Bostonian: 1.8 (1.001 – 3.2)'],
    'Meditation': ['Tried meditation: 11.6 (4.6–29.3)', 'Bostonian: 4.8 (1.9–12.3)', 'Female: 2.5 (1.3 – 4.8)', 'No associations', 'No associations', '', 'High expectations: 3.6 (1.7 – 7.7)', 'Tried meditation: 2.4 (1.3 – 4.5)', 'NOT QUERIED', ''],
    "T'ai chi": ['LOGISTIC NOT VALID**', '', 'No associations', 'LOGISTIC NOT VALID**', 'No associations', '', 'High expectations: 14.3 (5.4 – 38.3)', '', 'NOT QUERIED', ''],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
