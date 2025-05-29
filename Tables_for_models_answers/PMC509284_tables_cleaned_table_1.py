headers: (0,0);(0,1);(0,2)

import pandas as pd

df = pd.DataFrame({
    'Diagnosis': ['Non-specific chest pain', 'Anxiety', 'Angina', 'Myocardial infarction', 'Gastro-oesophageal pain', 'Musculo-skeletal pain', 'Other diagnosis', 'Not recorded'],
    'CPU care': ['144 (30.1%)', '13 (2.7%)', '63 (13.2%)', '28 (5.8%)', '74 (15.4%)', '122 (25.5%)', '26 (5.4%)', '9 (1.9%)'],
    'Routine care': ['125 (25.4%)', '21 (4.3%)', '123 (24.9%)', '27 (5.5%)', '60 (12.2%)', '106 (21.5%)', '18 (3.7%)', '13 (2.6%)'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7])
