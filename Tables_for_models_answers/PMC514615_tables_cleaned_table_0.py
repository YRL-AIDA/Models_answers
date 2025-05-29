headers: (0,0);(0,1);(0,2);(0,3);(0,4);(0,5);(0,6);(0,7)

import pandas as pd

df = pd.DataFrame({
    '': ['(A)', 'Round component', '(B)', 'Crescent component'],
    '': ['(A)', 'Round component', '(B)', 'Crescent component'],
    'Synaptophysin': ['++', '+'],
    'AE1/AE3': ['++', '-'],
    'Vimentin': ['++', '-'],
    'CD56': ['+', '-'],
    'chromogranin A': ['-', '-'],
    'MIB1': ['25%', '50%'],
}, index=[0, 1])
