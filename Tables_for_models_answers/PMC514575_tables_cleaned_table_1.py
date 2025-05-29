headers: (0,0);(0,1);(1,1);(1,2);(1,3);(1,4)

import pandas as pd

df = pd.DataFrame({
    'Genetic Model': ['Additive', 'Dominance', 'Reciprocal Heterozygote', 'Maternal Dominance', 'Paternal Polar Overdominance', 'Number of Animals'],
    '+/+': ['-1', '-1', '0', '-1', '-1', '6'],
    'CLPG Mat /+ Pat': ['0', '1', '-1', '2', '-1', '7'],
    '+ Mat / CLPG Pat': ['0', '1', '1', '0', '3', '8'],
    'CLPG Mat / CLPG Pat': ['1', '-1', '0', '-1', '-1', '8'],
}, index=[0, 1, 2, 3, 4, 5])
