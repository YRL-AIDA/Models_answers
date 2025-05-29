import pandas as pd

df = pd.DataFrame({
    'Level of Care': ['Government', '', '', '', 'Home', '', '', 'Non-Government', '', '', '', '', 'None', '', '', ''],
    'Provider': ['VHW', 'Dispensary', 'Health Centre', 'Hospital', 'Mothers', 'Family', 'Drug Shops', 'Dispensary', 'Health Centre', 'Hospital', 'TM at Practitioner', 'TM at Home', 'None', '', 'Number', 'Total'],
    '<5': ['0.0%', '19.4%', '20.0%', '5.3%', '2.5%', '9.4%', '8.1%', '10.3%', '1.6%', '2.2%', '6.6%', '2.8%', '11.9%', '100%', '320', ''],
    '5+': ['0.7%', '11.2%**', '14.4%*', '5.0%', '2.2%', '13.2%', '20.6%**', '5.5%*', '2.0%', '2.5%', '6.5%', '1.7%', '14.3%', '48%', '402', '722'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
