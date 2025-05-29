headers: (0,0);(0,1);(0,2);(0,3);(0,4);(0,5);(0,6)

import pandas as pd

df = pd.DataFrame({
    'Region': ['Banyo-Bankim', 'Banyo-Bankim', 'South of Central Province', 'South of Central Province', 'South of Central Province', 'South of Central Province', 'Lekie Department', 'Lekie Department', 'Lekie Department', 'Lekie Department', 'Mbam et Kim', 'Mbam et Kim', 'Western Province', 'Western Province'],
    'Sex*': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
    'Blood sample (μl)': ['50.00', '50.00', '30.00', '30.00', '50.00', '50.00', '30.00', '30.00', '50.00', '50.00', '30.00', '30.00', '50.00', '50.00'],
    'Prevalence of Loa loa': ['22.21', '20.00', '32.81', '27.37', '24.76', '18.49', '26.33', '19.10', '23.96', '21.41', '12.37', '4.53', '6.22', '3.76'],
    'Age range': ['5–98', '5–90', '5–80', '5–80', '5–86', '5–90', '5–91', '5–92', '5–80', '5–90', '5–99', '5–95', '15–99', '15–99'],
    'No. subjects': ['1783', '1815', '381', '453', '941', '1206', '1052', '1340', '359', '369', '1293', '1281', '916', '1036'],
    'No. villages': ['16', '', '5', '', '17', '', '14', '', '3', '', '24', '', '15', ''],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
