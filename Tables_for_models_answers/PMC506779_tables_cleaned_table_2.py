headers: (0,0);(0,1);(0,3);(0,4);(1,1);(1,2);(1,4);(1,5)

import pandas as pd

df = pd.DataFrame({
    'Injury type': ['Sprain', 'Contusion', 'Joint dysfunction', 'Sprain', 'Contusion', 'Strain', 'Laceration', '', 'Strain', '', 'Concussion', '', 'Abrasion', '', 'Epistaxis', '', 'Total', 'Total'],
    'Number': ['10', '3', '6', '1', '5', '1', '5', '', '4', '', '3', '', '1', '', '1', '', '35', '5'],
    'Rate': ['22.8', '15.2', '13.7', '5.1', '11.4', '5.1', '11.4', '', '9.1', '', '6.9', '', '2.3', '', '2.3', '', '79.9', '25.3'],
    'Injury type': ['Sprain', 'Contusion', 'Joint dysfunction', 'Sprain', 'Contusion', 'Strain', 'Laceration', '', 'Strain', '', 'Concussion', '', 'Abrasion', '', 'Epistaxis', '', 'Total', 'Total'],
    'Number': ['10', '3', '6', '1', '5', '1', '5', '', '4', '', '3', '', '1', '', '1', '', '35', '5'],
    'Rate': ['22.8', '15.2', '13.7', '5.1', '11.4', '5.1', '11.4', '', '9.1', '', '6.9', '', '2.3', '', '2.3', '', '79.9', '25.3'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8])
