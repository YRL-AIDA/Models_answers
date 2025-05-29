headers: (0,0);(0,1);(0,2);(0,3);(0,4);(0,5)

import pandas as pd

df = pd.DataFrame({
    '': ['Pool 1', 'Pool 2', 'Pool 3'],
    'sun exposure': ['1', '1', '0.7'],
    'coef water fill': ['4', '7', '4'],
    'water fix intake ( mm )': ['0', '0', '0'],
    'water fix lost ( mm )': ['0.01', '0.02', '0.028'],
    'max biomass density ( mg·m -2 )': ['30', '60', '70'],
}, index=[0, 1, 2])
