headers: (0,0);(0,1);(0,2);(0,3)

import pandas as pd

df = pd.DataFrame({
    'Peak control current amplitude (nA)': ['-1.52 ± 0.13', '-1.2 ± 0.14', '-1.19 ± 0.11'],
    'Pregabalin Concentration (μM)': ['0.025', '0.25', '2.5'],
    'Peak current in the presence of pregabalin (nA)': ['-0.98 ± 0.12 **', '-0.93 ± 0.18 *', '-0.94 ± 0.09***'],
    'Percentage inhibition and n value': ['31 ± 4 % (n = 8)', '22 ± 9 % (n = 6)', '21 ± 3 % (n = 26)'],
}, index=[0, 1, 2])
