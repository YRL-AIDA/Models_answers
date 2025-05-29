headers: (0,0);(0,1);(0,2);(0,3);(0,4);(0,5)

import pandas as pd

df = pd.DataFrame({
    '': ['n =', 'Time of survey', 'Weeks since last treatment', 'Hookworm', ' A. lumbricoides', ' T. trichiura', 'Hookworm', ' A. lumbricoides', ' T. trichiura'],
    'Post-Treatment 1 ‡': ['801', 'May/Jun 98', '3', '21.2', '1.0', '54.6', '77', '55', '227'],
    'Re-infection 1': ['790', 'Aug 98', '16', '24.8', '4.3', '50.9', '184', '115', '215'],
    'Post-Treatment 2 ‡': ['803', 'Oct/Nov 98', '3', '10.1', '0.7', '44.0', '14', '3', '116'],
    'Re-infection 2a': ['739', 'Feb 99', '18', '24.6', '3.0', '44.8', '65', '59', '174'],
    'Re-infection 2b': ['731', 'Apr/May 99', '29', '36.7', '8.6', '43.4', '139', '351', '175'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8])
