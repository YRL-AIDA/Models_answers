headers: (0,0);(0,1);(0,2);(0,3)

import pandas as pd

df = pd.DataFrame({
    'Cell Line': ['MDA-MB-231', 'MDA-MB-435', 'MDA-MB-436', 'MCF-7', 'NCI-adr', 'MCF-7stv', 'ML-20'],
    'Estrogen Receptor Status': ['-', '-', '-', '++', '-', '+', '+'],
    'Vimentin Expression': ['+', '+', '+', '-', '+', '-', '-'],
    'Invasiveness': ['+++', '++', '++', '+', '++', '+', '+'],
}, index=[0, 1, 2, 3, 4, 5, 6])
