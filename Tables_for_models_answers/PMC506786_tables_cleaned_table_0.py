headers: (0,0);(0,1)

import pandas as pd

df = pd.DataFrame({
    'Type of hyperplasia': ['Simple (cystic without atypia)', 'Complex (adenomatous without atypia)', 'Simple (cystic with atypia)', 'Complex (adenomatous with atypia)'],
    'Rate of progression': ['1', '3', '8', '29'],
}, index=[0, 1, 2, 3])
