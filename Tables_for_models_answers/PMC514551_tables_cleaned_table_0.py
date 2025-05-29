headers: (0,0);(0,1);(0,2);(0,3);(0,4)

import pandas as pd

df = pd.DataFrame({
    '': ['IHC', 'RT-PCR'],
    'FD/GM': ['15/17 (88%)', '1/1'],
    'Normal/Hyperplastic': ['33/42 (78%)', '1/1'],
    'DCIS': ['1/10 (10%)', '0/2'],
    'IC': ['2/45 (4%)', '13/35 (37%)'],
}, index=[0, 1])
