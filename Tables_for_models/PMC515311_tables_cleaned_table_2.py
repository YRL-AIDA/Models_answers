import pandas as pd

df = pd.DataFrame({
    'Model approach Predictors': ['- Age, per 10 years', '- Male sex', '- Age, per 10 years', '- Male sex', '- Hypertension', '- Diabetes mellitus', '- High cholesterol', '- Smoking', '- 10-year risk, per 5% increase'],
    'Coefficients (95% CI)': ['0.68 (0.63 – 0.73)', '0.72 (0.61 – 0.82)', '0.69 (0.64 – 0.73)', '0.73 (0.63 – 0.83)', '0.23 (0.14 – 0.32)', '0.48 (0.33 – 0.62)', '0.15 (0.05 – 0.24)', '0.45 (0.35 – 0.54)', '0.34 (0.31 – 0.36)'],
    'Corresponding percent increase in natural CAC scores*': ['97% (88 – 107%)', '105% (85 – 127%)', '99% (89 – 109%)', '108% (88 – 130%)', '26% (14 – 38%)', '61% (40 – 88%)', '16% (4.8 – 28%)', '56% (42 – 71%)', '40% (36 – 44%)'],
    'p-values': ['<0.001', '<0.001', '<0.001', '<0.001', '<0.001', '<0.001', '0.004', '<0.001', '<0.001'],
    'Adjusted R 2': ['0.14', '', '0.17', '', '', '', '', '', '0.11'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8])
