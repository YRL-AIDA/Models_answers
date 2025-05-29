headers: (0,0);(0,1);(0,2);(0,3);(0,4)

import pandas as pd

df = pd.DataFrame({
    'Group': ['Grade II', 'Grade III', 'Grade IV'],
    'Total tags': ['869,992', '1,026,620', '798,451'],
    'Unique tags a': ['22,574', '26,445', '33,541'],
    'Expressed tags per library b': ['3,999', '3,866', '3,518'],
    'Expressed in tumors and not in neural normals c': ['41', '55', '76'],
}, index=[0, 1, 2])
