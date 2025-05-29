import pandas as pd

df = pd.DataFrame({
    'Characteristic': ['Age (years)', 'Women', 'Hypertension*', 'High cholesterol*', 'Diabetes mellitus*', 'Smoking†', '- range', '- median, 25%–75%'],
    'N (%) or mean ± SD': ['54 ± 10 years', '3782 (40%)', '4069 (44%)', '5847 (63%)', '807 (9%)', '3679 (39%)', '1.0% – 74%', '11%, 7.0% – 15%'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7])
