import pandas as pd

df = pd.DataFrame({
    '': ['Age', 'Sex', 'Reference period', 'Diagnosis', 'Language', 'Region of residence'],
    'Population control': ['Within 5 year age group of case 1', 'The same sex as case', '', 'No history of cancer', 'Being capable to complete the interview in German', 'Residence matched to case 3'],
    'Ophthalmologist control': ['Within 5 year age group of case 1', 'The same sex as case', "Visit at the ophthalmologist's within 10 working days (possibly more) 2 before reference date set by case diagnosis.", 'No history of cancer', 'Being capable to complete the interview in German', 'Germany'],
    'Sibling control': ['Age within +/- ten years compared to age of case. If more then one sibling lies in this range, the one closest to the case is chosen, unless he/she refuses. If so, the sibling fitting second best in age is chosen.', 'The same sex as the case; when a same sex sibling does not exist or refused, then the opposite – sex sibling is chosen.', '', 'No history of cancer', 'Being capable to complete the interview in German', ''],
}, index=[0, 1, 2, 3, 4, 5])
