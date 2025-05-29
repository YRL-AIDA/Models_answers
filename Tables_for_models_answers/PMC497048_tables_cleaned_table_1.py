headers: (0,0);(0,1);(0,2);(0,3);(0,4)

import pandas as pd

df = pd.DataFrame({
    'Marker': ['P-onset', 'P amplitude', 'P-offset', 'QRS-onset', 'QRS amplitude', 'QRS-offset', 'T amplitude', 'T-offset'],
    'Tolerance SD ms': ['10.2', '', '12.7', '6.5', '', '11.6', '', '30.6'],
    'Non-Syntactic SD ms': ['22.6', '23.4', '16.7', '10.4', '14.3', '12.8', '19.2', '18.7'],
    'CC SD ms': ['22.1', '23.8', '19.7', '10.1', '1.8', '13.1', '21.4', '20.6'],
    'Multi-component based CC SD ms': ['11.9', '7.8', '11.6', '6.6', '1.8', '6.9', '8.2', '14.6'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7])
