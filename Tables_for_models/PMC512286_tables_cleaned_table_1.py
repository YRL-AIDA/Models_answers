import pandas as pd

df = pd.DataFrame({
    '': ['6MWT (m)', 'Age (years)', 'Weight (kg)', 'Height (cm)', 'BMI (kg/m 2 )'],
    'Male N = 53 mean (SD)': ['647.9 (201.8)', '64.1 (6.9)', '80.5 (11.0)', '171.3 (6.6)', '27.4 (3.1)'],
    'Female N = 103 mean (SD)': ['579.3 * (159.8)', '65.5 (7.7)', '69.4 † (11.4)', '158.2 † (6.3)', '27.8 (4.2)'],
}, index=[0, 1, 2, 3, 4])
