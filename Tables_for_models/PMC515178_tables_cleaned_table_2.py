import pandas as pd

df = pd.DataFrame({
    '': ['Normotensive women', 'All hypertensive women', 'Mild PIH', 'Severe PIH', 'HELLP', 'Eclampsia', 'Chronic Hypertension', 'Chronic hypertension and PIH'],
    'Total No.': ['122,855', '14,013', '10,683', '1,826', '214', '32', '773', '485'],
    'No.': ['461', '73', '44', '12', '2', '0', '7', '8'],
    '%': ['0.4', '0.52', '0.4', '0.7', '0.9', '0.0', '0.9', '1.7'],
    'Relative Risk': ['1.0', '1.4', '1.1', '1.8', '2.5', '-', '2.4', '4.4'],
    '95% CI': ['-', '1.1,1.8', '0.8,1.5', '1.0,3.1', '0.6,9.9', '0.0,41.0', '1.2,5.1', '2.2,8.8'],
    'P value': ['-', '0.01', '0.55', '0.50', '0.19', '1.00', '0.03', '<0.001'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7])
