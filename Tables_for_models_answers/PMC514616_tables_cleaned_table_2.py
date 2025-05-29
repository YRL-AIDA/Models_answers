headers: (0,0);(0,1)

import pandas as pd

df = pd.DataFrame({
    'Fertilization protocol': ['Sperm solution dripped over the eggs', 'Testes minced directly over eggs', 'Sperm solution injected under the jelly coat', 'Sperm incubated in jelly buffer and then injected under the jelly coat', 'Poked, then fertilized 15 minutes later by mincing testes directly over the eggs'],
    'Number that developed to neurula/Number tested (%)': ['5/63 (8)', '8/30 (27)', '0/12', '1/10 (10)', '0/36'],
}, index=[0, 1, 2, 3, 4])
