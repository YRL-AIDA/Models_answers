import pandas as pd

df = pd.DataFrame({
    'Egg origin': ['Eggs laid in response to hormone treatment', '', '', 'Oocytes dissected directly from ovisac', '', '', ''],
    'Treatment': ['Undisturbed', 'Poked', 'A23187', 'Undisturbed', 'A23187', 'Progesterone', 'Progesterone & AA23187'],
    'Number cleaving at 10 hours/Number tested (%)': ['11/32 (34)', '28/44 (64)', '30/36 (83)', '0/40', '0/40', '0/40', '0/40'],
    'Number cleaving at 16 hours, after being poked at 10 hours/Number tested (%)': ['6/8 (75)', '-', '-', '-', '-', '-', '-'],
}, index=[0, 1, 2, 3, 4, 5, 6])
