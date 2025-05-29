headers: (0,0);(0,1);(1,1);(1,2)

import pandas as pd

df = pd.DataFrame({
    'SES Variables': ['Percent Unemployed b', 'Median Income a', 'Median Rent a', 'Median House Value a', 'Percent Working Class b', 'Percent with a High School Diploma a', 'Percent Below the Poverty Level b'],
    'Wealth SES': ['0.099', '0.895', '0.923', '0.835', '-0.405', '0.919', '-0.269'],
    'Poverty SES': ['0.932', '-0.294', '-0.037', '-0.264', '0.671', '-0.081', '0.828'],
}, index=[0, 1, 2, 3, 4, 5, 6])
