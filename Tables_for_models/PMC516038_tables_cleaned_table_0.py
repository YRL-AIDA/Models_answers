import pandas as pd

df = pd.DataFrame({
    '': ['Age (yrs)', 'Mean (SD)', '', 'Range', 'Height (m)', 'Mean (SD)', '', 'Range', 'Weight (kg)', 'Mean (SD)', '', 'Range', 'Years as a PT', 'Mean (SD)', '', 'Range', 'Hours per week in direct patient care', 'Mean (SD)', '', 'Range'],
    '': ['Age (yrs)', 'Mean (SD)', '', 'Range', 'Height (m)', 'Mean (SD)', '', 'Range', 'Weight (kg)', 'Mean (SD)', '', 'Range', 'Years as a PT', 'Mean (SD)', '', 'Range', 'Hours per week in direct patient care', 'Mean (SD)', '', 'Range'],
    'Female (n = 92)': ['30.3 (7.5)', '22 – 55', '1.63 (6.21)', '1.32 – 1.78', '57.9 (6.4)', '45 – 82', '8.2 (6.7)', '2 – 29', '38.5 (9.0)', '8 – 60'],
    'Male (n = 28)': ['30.8 (4.4)', '25 – 38', '1.76 (7.3)', '1.65 – 1.90', '78.1 (13.1)', '53 – 100', '7.9 (3.6)', '2 – 14', '40.0 (9.8)', '5 – 60'],
    'All': ['30.4 (6.9)', '22 – 55', '1.67 (8.41)', '1.32 – 1.90', '62.6 (12.0)', '45 – 100', '8.0 (6.0)', '2 – 29', '38.8 (9.2)', '5 – 60'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
