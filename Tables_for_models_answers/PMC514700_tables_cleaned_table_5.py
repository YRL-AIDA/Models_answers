headers: (0,0);(0,1);(0,3);(1,1);(1,2);(1,3);(1,4)

import pandas as pd

df = pd.DataFrame({
    '': ['Number of all CDSs', 'CDSs shared by both programs', 'CDSs merely identified by the respective program'],
    'CRITICA': ['6734', '5135', '6332*', '4823', '402', '312'],
    'IdentiCS': ['5650', '5261', '4302', '4512', '1348', '749'],
    'CRITICA': ['6734', '5135', '6332*', '4823', '402', '312'],
    'IdentiCS': ['5650', '5261', '4302', '4512', '1348', '749'],
}, index=[0, 1, 2])
