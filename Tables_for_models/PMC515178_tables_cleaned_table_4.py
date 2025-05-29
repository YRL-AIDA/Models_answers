import pandas as pd

df = pd.DataFrame({
    '': ['Normotensive women', 'Gestational hypertension without proteinuria', 'Gestational hypertension with proteinuria', 'Pre-existing hypertension', 'Twins', 'Gestational hypertension without proteinuria × twins', 'Gestational hypertension with proteinuria × twins', 'Pre-existing hypertension × twins', 'Smoking', 'Gestational hypertension without proteinuria × smoking', 'Gestational hypertension with proteinuria × smoking', 'Pre-existing hypertension × smoking', 'Normotensive women', 'Gestational hypertension without proteinuria', 'Gestational hypertension with proteinuria', 'Pre-existing hypertension', 'Smoking', 'Gestational hypertension without proteinuria × smoking', 'Gestational hypertension with proteinuria × smoking', 'Pre-existing hypertension × smoking'],
    'Odds ratio': ['1.0', '1.5', '3.7', '2.5', '4.7', '0.7', '0.3', '0.7', '2.9', '1.0', '0.9', '0.6', '1.0', '0.8', '1.4', '3.5', '1.4', '2.5', '1.8', '0.6'],
    '95% CI': ['-', '1.4,1.6', '3.3,4.1', '2.1,3.0', '4.3,5.2', '0.6,0.9', '0.2,0.4', '0.3,1.4', '2.8,3.0', '0.9,1.2', '0.7,1.1', '0.4,0.8', '-', '0.5,1.2', '0.6,2.9', '2.0,6.2', '1.2,1.7', '1.3,4.7', '0.4,5.3', '0.1,2.5'],
    'P value': ['-', '<0.001', '<0.001', '<0.001', '<0.001', '0.01', '<0.001', '0.29', '<0.001', '0.96', '0.28', '0.002', '-', '0.24', '0.42', '<0.001', '<0.001', '0.006', '0.33', '0.43'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
