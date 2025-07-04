import pandas as pd

df = pd.DataFrame({
    'Variable': ['Intercept', 'Nicotine yield by machine', 'Number of cigarettes consumed', 'Interaction', 'Intercept', 'Nicotine yield by machine', 'FTND score', 'Interaction'],
    'B': ['5.270', '0.762', '0.045', '-0.012', '4.994', '0.793', '0.268', '-0.079'],
    'p': ['<0.001', '', '0.001', '<0.001', '<0.001', '<0.001', '0.16', '', '<0.001', '', '0.001', '<0.001', '<0.001', '<0.001', '0.057', ''],
    'r': ['', '0.23', '0.43', '', '', '0.18', '0.52', ''],
    'p': ['<0.001', '', '0.001', '<0.001', '<0.001', '<0.001', '0.16', '', '<0.001', '', '0.001', '<0.001', '<0.001', '<0.001', '0.057', ''],
}, index=[0, 1, 2, 3, 4, 5, 6, 7])
