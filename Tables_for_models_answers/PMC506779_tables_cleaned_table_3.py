headers: (0,0);(0,3);(1,0);(1,1);(1,2);(1,3);(1,4);(1,5)

import pandas as pd

df = pd.DataFrame({
    'Injury mechanism': ['Receiving a kick', 'Delivering a kick', 'Delivering a kick', 'Receiving a kick', 'Simultaneous kicks', 'Not recorded', 'Other', '', 'Not recorded', '', 'Total', 'Total'],
    'No': ['12', '2', '7', '1', '1', '2', '3', '', '12', '', '35', '5'],
    'Rate': ['27.4', '10.1', '16.0', '5.1', '2.3', '10.1', '6.9', '', '27.4', '', '79.9', '25.3'],
    'Injury mechanism': ['Receiving a kick', 'Delivering a kick', 'Delivering a kick', 'Receiving a kick', 'Simultaneous kicks', 'Not recorded', 'Other', '', 'Not recorded', '', 'Total', 'Total'],
    'No': ['12', '2', '7', '1', '1', '2', '3', '', '12', '', '35', '5'],
    'Rate': ['27.4', '10.1', '16.0', '5.1', '2.3', '10.1', '6.9', '', '27.4', '', '79.9', '25.3'],
}, index=[0, 1, 2, 3, 4, 5])
