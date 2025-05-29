import pandas as pd

df = pd.DataFrame({
    'Specimen': ['Sinus', 'Nasopharynx 1', 'Total'],
    'S. pneumoniae': ['272 (47.5)', '368 (48.1)', '640 (47.9)'],
    'H. influenzae': ['148 (25.9)', '181 (23.7)', '329 (24.6)'],
    'M. catarrhalis': ['67 (11.7)', '145 (19.0)', '212 (15.9)'],
    'S. aureus': ['64 (11.2)', '52 (6.8)', '116 (8.7)'],
    'S. pyogenes': ['21 (3.7)', '18 (2.4)', '39 (2.9)'],
    'Total': ['572 (42.8)', '764 (57.2)', '1336 (100)'],
}, index=[0, 1, 2])
