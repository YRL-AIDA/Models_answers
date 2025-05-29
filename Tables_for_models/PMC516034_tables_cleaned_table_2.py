import pandas as pd

df = pd.DataFrame({
    '': ['Complete response, n (%)', 'Partial response, n (%)', 'Stable disease, n (%)', 'Progressive disease, n (%)', 'Early death, n (%)', 'Response rate, % (95% CI)', 'Disease control rate, % (95% CI)'],
    'Patients': ['1 (3.2)', '10 (32.3)', '7 (22.6)', '11 (35.5)', '2 (6.5)', '35.5 (18.6–52.3)', '58.1 (49.2–67.0)'],
}, index=[0, 1, 2, 3, 4, 5, 6])
