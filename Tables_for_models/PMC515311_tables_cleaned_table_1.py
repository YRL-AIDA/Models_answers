import pandas as pd

df = pd.DataFrame({
    'Modeling approach Predictors': ['- Age, per 10 years', '- Male sex', '- Age, per 10 years', '- Male sex', '- Hypertension', '- Diabetes mellitus', '- High cholesterol', '- Smoking', '- 10-year risk, per 5% increase in the Framingham 10-year CHD risk estimate'],
    'Odds ratio (95% CI)': ['2.83 (2.67 – 2.99)', '3.60 (3.26 – 3.96)', '2.78 (2.62 – 2.94)', '3.67 (3.31 – 4.06)', '1.51 (1.37 – 1.66)', '1.85 (1.55 – 2.21)', '1.40 (1.27 – 1.54)', '1.71 (1.56 – 1.89)', '1.96 (1.88 – 2.04)'],
    'p-value': ['<0.001', '<0.001', '<0.001', '<0.001', '<0.001', '<0.001', '<0.001', '<0.001', '<0.001'],
    'C-statistic': ['0.76', '', '0.78', '', '', '', '', '', '0.74'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8])
