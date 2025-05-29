headers: (0,0);(0,1);(0,2)

import pandas as pd

df = pd.DataFrame({
    '': ['Upper ureter', 'Middle ureter', 'Distal ureter'],
    'Stone identified/total': ['2/6 (33%)', '9/14 (64%)', '1/2 (50%)'],
    'Mean size': ['6 mm', '5 mm', '7 mm'],
}, index=[0, 1, 2])
