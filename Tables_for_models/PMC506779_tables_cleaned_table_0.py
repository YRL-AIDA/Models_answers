import pandas as pd

df = pd.DataFrame({
    '': ['Number of athletes', 'Number of reported injuries', 'Number of athlete-exposures (AE)', '-- per 100 athletes', '-- per 1,000 AE'],
    'Men': ['219', '35', '438', '16.0 (10.7–21.3)', '79.9 (53.4–106.4)'],
    'Women': ['99', '5', '198', '5.1 (0.7–9.5)', '25.3 (3.2–47.4)'],
    'Total': ['318', '40', '636', '12.6 (8.7–16.5)', '62.9 (43.4–82.4)'],
}, index=[0, 1, 2, 3, 4])
