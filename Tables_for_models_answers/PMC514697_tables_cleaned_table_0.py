headers: (0,0);(1,0);(1,1);(1,2);(1,3);(1,4);(1,5)

import pandas as pd

df = pd.DataFrame({
    'csr-PK': ['135', 'internal loop', '23'],
    '1-nt bulge': ['11', 'triple helix', '12'],
    'Rule 2 violated': ['6', 'four helices', '1'],
    'isolated basepair': ['17', 'kissing hairpins', '3'],
    'G-A basepair': ['3', 'large bulge', '1'],
    'total': ['172', 'total', '40'],
}, index=[0, 1, 2])
