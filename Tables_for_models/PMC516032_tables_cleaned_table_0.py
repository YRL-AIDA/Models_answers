import pandas as pd

df = pd.DataFrame({
    '': ['N', 'Male', '<35 years', '35–44', '45–54', '55 +', 'Urban/Metropolitan practice', 'Solo practice', '5 plus GPs in practice'],
    'GP sample': ['379', '61.4%', '8.2%', '29.3%', '36.7%', '25.9%', '76.0%', '16.1%', '45.2%'],
    'Australian population of GPs (a)': ['17,534', '67.5%', '12.1%', '27.1%', '32.0%', '28.8%', '72.6%', 'Not available', 'Not available'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8])
