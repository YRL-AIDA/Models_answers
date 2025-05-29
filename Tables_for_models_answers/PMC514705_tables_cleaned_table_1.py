headers: (0,0);(0,1);(0,2);(0,3);(0,4);(0,5)

import pandas as pd

df = pd.DataFrame({
    '': ['Acute vomiting', 'Alopecia', 'Leucopenia', 'Alopecia+Acute vomiting'],
    'Total N = 50': ['63.3%', '60%', '10%', '46.7%'],
    'Clinical responders N = 35': ['81%(p = 0.002)', '86%(p = 0.000)', '14%(NS)', '67%(p = 0.001)'],
    'Clinical non-responders N = 15': ['22.2%', '0%', '0%', '0%'],
    'Immuno-histochemical responders N = 30': ['78%(p = 0.04)', '94%(p = 0.000)', '17%(NS)', '72%(p = 0.001)'],
    'Immuno-histochemical non-responders N = 20': ['41.7%', '8.3%', '0%', '8.3%'],
}, index=[0, 1, 2, 3])
