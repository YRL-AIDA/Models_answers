headers: (0,0);(0,1);(0,2)

import pandas as pd

df = pd.DataFrame({
    'Clutch': ['1', '2', '3', '4', 'Total'],
    'Number of eggs laid': ['39', '58', '30', '42', '169'],
    'Number that developed to neurula (%)': ['24 (62)', '36 (62)', '28 (93)', '34 (81)', '122 (72)'],
}, index=[0, 1, 2, 3, 4])
