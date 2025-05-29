headers: (0,0);(0,1);(0,2);(1,2);(1,3)

import pandas as pd

df = pd.DataFrame({
    'Level of Care': ['Government', '', '', '', 'Home', '', '', 'Non-Government', '', '', '', '', ''],
    'Provider': ['VHW*', 'Dispensary', 'Health Centre', 'Hospital', 'Mothers', 'Family', 'Drug Shops', 'Dispensary', 'Health Centre', 'Hospital', 'TM** at Practitioner', 'TM** at Home', 'Total care seeking'],
    'No.': ['5', '92', '104', '67', '19', '64', '36', '77', '39', '30', '73', '27', '633'],
    '%': ['0.8%', '14.5%', '16.4%', '10.6%', '3.0%', '10.1%', '5.7%', '12.2%', '6.2%', '4.7%', '11.5%', '4.3%', '100.0%'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
