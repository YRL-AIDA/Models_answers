import pandas as pd

df = pd.DataFrame({
    'Health problem (a) (n)': ['Anxiety (381)', 'Depression (1,100)', 'Back complaint (578)', 'Diabetes (706)', 'Ischaemic heart disease (585)', 'Asthma (876)', 'Oesophageal disease (636)', 'Osteoarthritis (859)', 'Hypertension (2,094)'],
    'Mean annual visits': ['14.1', '13.1', '12.8', '13.7', '14.3', '10.5', '12.9', '13.0', '11.8'],
    'No. other problems': ['3.4', '3.2', '2.9', '3.8', '4.3', '2.8', '4.1', '4.1', '3.5'],
    'Morbidity coefficient (b) (95%CI)': ['2.7 (0.9;4.5)', '2.2 (1.4;3.1)', '2.4 (0.6;4.2)', '0.9 (-0.1;1.9)', '0.6 (-0.7;1.9)', '0.3 (-0.4;1.0)', '-0.2 (-1.2;0.8)', '-0.4 (-1.3;0.5)', '-0.4 (-1.2;0.4)'],
    'p-value': ['0.003 †', '<.0001 †', '0.009 †', '0.08', '0.38', '0.40', '0.65', '0.39', '0.30'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8])
