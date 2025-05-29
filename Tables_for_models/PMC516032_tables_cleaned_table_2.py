import pandas as pd

df = pd.DataFrame({
    'Patient characteristics (n)': ['Highly accessible (8,702)', 'Moderately accessible (1,599)', 'Remote/very remote (145)', 'Concession health care card holder (4,448)', 'Non health care card holder (6,307)', 'Speaks language other than English at home (890)', 'Speaks English at home (9,865)', 'Male (4,285)', 'Female (6,404)'],
    'Mean problems': ['2.9', '2.7', '2.5', '3.5', '2.4', '2.8', '2.9', '2.7', '2.9'],
    'Crude Mean visits': ['9.1', '7.7', '5.8', '11.4', '6.8', '9.0', '8.7', '8.5', '8.9'],
    'Mean visits': ['9.0', '7.9', '6.5', '10.7', '7.5', '9.1', '8.8', 'N/A', 'N/A'],
    'p-value': ['', '0.05', '<.0001', '<.0001', '', '0.369', '', 'N/A', ''],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8])
