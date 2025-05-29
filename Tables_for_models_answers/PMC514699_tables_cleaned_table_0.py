headers: (0,0);(0,1);(0,2);(0,3)

import pandas as pd

df = pd.DataFrame({
    '': ['Affy', 'Alt1', 'Alt2'],
    'Affy': ['', '61', '54'],
    'Alt1': ['61', '', '95'],
    'Alt2': ['54', '95', ''],
}, index=[0, 1, 2])
