import pandas as pd

df = pd.DataFrame({
    '': ['Predicted prevalence', 'First dataset', '<20%', '', '(collected by IRD-CPC)', '≥ 20%', '', 'Dataset used for validation', '<20%', '', '(collected by TDR)', '≥ 20%'],
    '': ['Predicted prevalence', 'First dataset', '<20%', '', '(collected by IRD-CPC)', '≥ 20%', '', 'Dataset used for validation', '<20%', '', '(collected by TDR)', '≥ 20%'],
    '': ['Predicted prevalence', 'First dataset', '<20%', '', '(collected by IRD-CPC)', '≥ 20%', '', 'Dataset used for validation', '<20%', '', '(collected by TDR)', '≥ 20%'],
    '<20%': ['48', '12', '20', '18'],
    '≥ 20%': ['8', '27', '5', '31'],
}, index=[0, 1, 2, 3])
