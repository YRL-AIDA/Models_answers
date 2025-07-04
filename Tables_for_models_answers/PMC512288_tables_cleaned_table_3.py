headers: (0,0);(0,1);(1,1);(1,2);(1,3);(1,4);(1,5);(1,6);(1,7)

import pandas as pd

df = pd.DataFrame({
    'MARKER': ['D12S85', 'D12S1706', 'D12S346', 'D12S78', 'D12S79', 'D12S86', 'D18S59', 'D18S481', 'D18S63', 'D18S452', 'D18S53', 'D18S474'],
    '0': ['-7.5', '-36.21', '-32.76', '-27.99', '-38.53', '-39.59', '-35.34', '-32.69', '-36.39', '-34.97', '-38.03', '-29.88'],
    '0.01': ['-6.71', '-28.66', '-24.46', '-20.59', '-30.26', '-31.68', '-27.25', '-24', '-28.55', '-25.21', '-26.36', '-22.79'],
    '0.05': ['-4.62', '-17.67', '-13.34', '-10.1', '-18.47', '-19.83', '-16.82', '-14.58', '-17.92', '-15.47', '-14.65', '-14.41'],
    '0.1': ['-2.56', '-10.77', '-7.11', '-4.65', '-11.21', '-12.58', '-10.69', '-9.19', '-11.36', '-9.72', '-8.62', '-9.29'],
    '0.2': ['-0.44', '-3.85', '-1.68', '-0.46', '-4.12', '-5.12', '-4.4', '-3.73', '-4.65', '-3.78', '-3.15', '-3.98'],
    '0.3': ['0.19', '-1.04', '-0.04', '0.43', '-1.24', '-1.8', '-1.51', '-1.26', '-1.63', '-1.22', '-0.94', '-1.45'],
    '0.4': ['0.17', '-0.15', '0.11', '0.24', '-0.26', '-0.45', '-0.26', '-0.24', '-0.35', '-0.23', '-0.14', '-0.31'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
