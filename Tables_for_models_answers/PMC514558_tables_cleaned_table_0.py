headers: (0,0);(0,1);(0,2);(0,3);(0,4);(0,5)

import pandas as pd

df = pd.DataFrame({
    'Scale': ['SF', 'DA', 'L', 'WS', 'PR', 'T'],
    'No. of items per scale': ['2', '2', '2', '1', '2', '1'],
    'Convergent validity (range of correlation)': ['0.69–0.78', '0.71–0.78', '0.67–0.88', '1.00', '0.50–0.99', '1.00'],
    'Scaling Success 1': ['2/2', '2/2', '2/2', '1/1', '2/2', '1/1'],
    'Scaling Success Rate 2': ['100', '100', '100', '100', '100', '100'],
    "Internal consistency (Cronbach's α)": ['0.70', '0.76', '0.71', '1.00', '0.79', '1.00'],
}, index=[0, 1, 2, 3, 4, 5])
