headers: (0,0);(0,1);(0,2);(0,3)

import pandas as pd

df = pd.DataFrame({
    'Out come': ['Chorioamnionitis', 'Early onset sepsis', 'RDS', 'Neonatal death'],
    'AFI<5(26)': ['5(19/2%)', '7(30/4%)', '6(26/1%)', '4(17/4%)'],
    'AFI ≥ 5 (69)': ['2 (3%)', '19(27/9%)', '8 (11/8%)', '5(7/4%)'],
    'Statistical significant': ['p < 0/001', 'p = 0.819', 'p = 0.1', 'p = 0.163'],
}, index=[0, 1, 2, 3])
