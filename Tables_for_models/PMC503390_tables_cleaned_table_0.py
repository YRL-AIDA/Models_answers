import pandas as pd

df = pd.DataFrame({
    '': ['Number of wards a', 'Range of ward Townsend scores', 'Number of cases b (all ages)', 'Total population c (all ages)', 'Incidence [corrected] d (cases /100,000 /yr)', 'Incidence relative risk compared to least deprived wards [CI]'],
    'Least deprived wards': ['384', '-6.26 to -2.19', '88', '1,473,272', '3.0 [5.1] (2.4 – 3.7) e', '1.00'],
    'Intermediate wards': ['383', '-2.2 to-0.33', '97', '1,506,359', '3.2 [5.5] (2.6 – 3.9)', '1.07 [0.80–1.43]'],
    'Most deprived wards': ['384', '0.34 to 8.44', '267', '2,271,294', '5.9 [10.1) (5.2 – 6.6)', '1.97 [1.55–2.51]'],
}, index=[0, 1, 2, 3, 4, 5])
