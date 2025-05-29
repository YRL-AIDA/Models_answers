import pandas as pd

df = pd.DataFrame({
    'Topical analgesic': ['NSAID', 'Salicylates', 'Capsaicin'],
    'Trials': ['14', '6', '3'],
    'Patients': ['1502', '429', '368'],
    'Treatment': ['48', '54', '38'],
    'Placebo': ['26', '36', '25'],
    'NNT (95% CI)': ['4.6 (3.8 to 5.9)', '5.3 (3.6 to 10)', '8.1 (4.6 to 34)'],
}, index=[0, 1, 2])
