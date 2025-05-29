headers: (0,0);(0,1);(0,2)

import pandas as pd

df = pd.DataFrame({
    'Database': ['True positive', 'False positive', 'False negative', 'Sensitivity %*', 'Specificity %*', 'Inconsistence rate (%) in TP'],
    'KEGG': ['4121', '907', '328', '92.6 (91.1)', '82.0 (94.9)', '0.35'],
    'SW': ['4339', '987', '110', '97.7 (98.2)', '81.5 (87.2)', '0.64'],
}, index=[0, 1, 2, 3, 4, 5])
