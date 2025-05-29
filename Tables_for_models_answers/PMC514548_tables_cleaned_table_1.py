headers: (0,0);(0,1);(0,2);(0,3)

import pandas as pd

df = pd.DataFrame({
    '': ['Baseline Survey', 'After Treatment 1', 'After Treatment 2', '1 Treatment', '2 Treatments', 'Baseline Survey', 'After Treatment 1', 'After Treatment 2', '1 Treatment', '2 Treatments'],
    'Hookworm': ['82.9', '17.6', '5.7', '78.8', '93.2', '881', '60', '11', '93.2', '98.8'],
    'A. lumbricoides': ['22.0', '0.8', '0.5', '96.4', '97.7', '2213', '52', '3', '97.7', '99.8'],
    'T. trichiura': ['59.8', '52.2', '39.9', '12.7', '33.3', '319', '240', '166', '24.8', '47.8'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
