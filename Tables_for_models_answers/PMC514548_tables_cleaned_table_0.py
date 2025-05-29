headers: (0,0);(0,1);(0,2);(0,3)

import pandas as pd

df = pd.DataFrame({
    '': ['n =', 'Median Age (Inter quartile range)', 'Hookworm', 'A. lumbricoides', 'T. trichiura', 'Hookworm', 'A. lumbricoides', 'T. trichiura'],
    'Males': ['445', '11.2 (10.1–12.3)', '86.5', '15.7', '57.3', '984', '876', '240'],
    'Females': ['572', '10.7 (9.7–11.8)', '80.6', '22.2', '57.2', '792', '2948', '332'],
    'M/F Ratio* (95%CI or P )': ['', '', '1.07 (1.02 to 1.13)', '0.71 (0.54 to 0.92)', '1.00 (0.90 to 1.12)', '1.24 ( P < 0.001)', '0.30 ( P = 0.008)', '0.72 ( P = 0.671)'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7])
