import pandas as pd

df = pd.DataFrame({
    'Pop': ['NE', 'MO', 'CA', 'OB', 'IB', 'LY', 'GO', 'MU', 'BB', 'PL', 'VN', 'TK', 'GD'],
    'HS': ['0.079', '0.049', '0.029', '0.044', '0.044', '0.047', '0.066', '0.076', '0.043', '0.061', '0.045', '0.047', '0.064'],
    'NE': ['', '0.123', '0.086', '0.092', '0.091', '0.096', '0.122', '0.118', '0.101', '0.11', '0.105', '0.096', '0.112'],
    'MO': ['', '', '0.07', '0.052', '0.041', '0.047', '0.072', '0.078', '0.052', '0.067', '0.042', '0.053', '0.064'],
    'CA': ['', '', '', '0.04', '0.04', '0.04', '0.07', '0.07', '0.05', '0.07', '0.04', '0.05', '0.06'],
    'OB': ['', '', '', '', '0.03', '0.03', '0.055', '0.066', '0.038', '0.064', '0.034', '0.044', '0.051'],
    'IB': ['', '', '', '', '', '0.026', '0.036', '0.051', '0.031', '0.05', '0.023', '0.028', '0.036'],
    'LY': ['', '', '', '', '', '', '0.047', '0.056', '0.037', '0.056', '0.028', '0.029', '0.043'],
    'GO': ['', '', '', '', '', '', '', '0.054', '0.054', '0.075', '0.039', '0.052', '0.057'],
    'MU': ['', '', '', '', '', '', '', '', '0.068', '0.077', '0.053', '0.062', '0.073'],
    'BB': ['', '', '', '', '', '', '', '', '', '0.063', '0.037', '0.044', '0.054'],
    'PL': ['', '', '', '', '', '', '', '', '', '', '0.049', '0.052', '0.059'],
    'VN': ['', '', '', '', '', '', '', '', '', '', '', '0.032', '0.032'],
    'TK': ['', '', '', '', '', '', '', '', '', '', '', '', '0.043'],
    'GD': ['', '', '', '', '', '', '', '', '', '', '', '', ''],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
