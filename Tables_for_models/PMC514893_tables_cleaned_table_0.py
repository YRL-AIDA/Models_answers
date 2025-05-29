import pandas as pd

df = pd.DataFrame({
    'Cell Line': ['Jurkat-Neo', 'Jurkat-CXCR3', 'Jurkat-Bcl2'],
    'CD3': ['98 (138)', '98 (154)', '96 (144)'],
    'CXCR4': ['99 (118)', '99 (124)', '96 (124)'],
    'CXCR3': ['2 (5)', '99 (24)', '5 (6)'],
    'CXCR2': ['4 (4)', '5 (8)', '7 (5)'],
}, index=[0, 1, 2])
