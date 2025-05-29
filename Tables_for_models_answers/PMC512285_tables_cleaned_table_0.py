headers: (0,0);(0,1);(1,1);(1,2)

import pandas as pd

df = pd.DataFrame({
    'Patient characteristic': ['Mean age (SD)', 'Sex n (%) Male', ' Congestive heart failure %', ' Angina %', ' Hypertension %', ' Diabetes mellitus %', ' Impaired mobility %', ' Smoking %', 'Impaired left ventricular function %'],
    'Cardiologist (N = 275)': ['64.4 (SD 12.8)', '275 (71.4)', '11.3', '94.9', '41.8', '12.1', '7.8', '36.0', '24.6'],
    'Non Cardiologist (N = 201)': ['74.8 (SD 11.4)', '201 (52.8)', '29.6', '86.7', '46.6', '17.1', '17.7', '49.6', '25.0'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8])
