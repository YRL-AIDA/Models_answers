import pandas as pd

df = pd.DataFrame({
    'Characteristics': ['No. Patients', 'Gender, male/female', 'median age, years (range)', 'Colon', 'Rectum', 'Ileum', 'Liver', 'Lung', 'Lymph nodes', 'Local relapse', 'other sites', 'Peritoneum', '1', '2', '≥3', 'surgery only', 'surgery+radiotherapy+adjuvant chemotherapy', 'surgery+adjuvant chemotherapy'],
    'No.': ['35', '25/10', '62 (38–75)', '21', '12', '1', '26', '12', '6', '3', '3', '8', '14', '17', '4', '28', '1', '5'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
