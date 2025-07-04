headers: (0,0);(0,1);(0,2);(0,3);(0,4);(0,6);(0,8);(1,4);(1,5);(1,6);(1,7)

import pandas as pd

df = pd.DataFrame({
    'Patient': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Controls'],
    'Age (years) / Gender': ['38 / M', '30 / M', '56 / M', '57 / F', '44 / M', '26 / M', '47 / M', '25 / M', '37 / F', '35 / M', '( n = 10)'],
    'Type of brain injury (Marshall score)': ['EML', 'DI II°', 'EML', 'DI II°', 'EML', 'EML', 'EML', 'EML', 'DI III°', 'DI II°', ''],
    'Outcome (GOS)': ['4', '3', '4', '5', '4', '4', '1', '4', '3', '4', ''],
    'Mean': ['6.4', '40.6', '3.6', '114.3', '6.3', '35.1', '6.0', '20.1', '1.6', '39.8', '3.2', '108.5', '1.1', '268.5', '2.2', '91.6', '1.6', '183.7', '2.0', '209.4', '1.0', '5.0'],
    'Range': ['1.0 – 11.5', '6.5 – 155.2', '1.0 – 7.7', '29.7 – 286.4', '1.0 – 10.0', '11.2 – 100.3', '1.0 – 11.7', '5.0 – 168.8', '1.0 – 3.4', '22.6 – 74.5', '1.0 – 10.3', '5.0 – 328.6', '1.0 – 1.4', '78.3 – 462.0', '1.0 – 4.0', '10.3 – 290.0', '1.0 – 2.7', '21.5 – 382.2', '1.0 – 5.8', '19.9 – 391.8', '1.0 – 7.1', '5.0 – 8.4'],
    'Mean': ['6.4', '40.6', '3.6', '114.3', '6.3', '35.1', '6.0', '20.1', '1.6', '39.8', '3.2', '108.5', '1.1', '268.5', '2.2', '91.6', '1.6', '183.7', '2.0', '209.4', '1.0', '5.0'],
    'Range': ['1.0 – 11.5', '6.5 – 155.2', '1.0 – 7.7', '29.7 – 286.4', '1.0 – 10.0', '11.2 – 100.3', '1.0 – 11.7', '5.0 – 168.8', '1.0 – 3.4', '22.6 – 74.5', '1.0 – 10.3', '5.0 – 328.6', '1.0 – 1.4', '78.3 – 462.0', '1.0 – 4.0', '10.3 – 290.0', '1.0 – 2.7', '21.5 – 382.2', '1.0 – 5.8', '19.9 – 391.8', '1.0 – 7.1', '5.0 – 8.4'],
    'Correlation r S': ['- 0.804 **', '- 0.580 *', '- 0.530', '- 0.761 **', '- 0.751 *', '- 0.832 **', '- 0.372', '- 0.195', '- 0.844 **', '- 0.772 *', ''],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
