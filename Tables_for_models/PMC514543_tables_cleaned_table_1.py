import pandas as pd

df = pd.DataFrame({
    'Sr. No.': ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
    'Source': ['Saskatoon', 'Saskatoon', 'USDA', 'USDA', 'Saskatoon', 'USDA', 'USDA', 'USDA', 'Saskatoon'],
    'TMP\\PI No.': ['TMP = 8704', 'TMP = 8738', 'PI = 345743', 'PI = 244288', 'TMP = 8750', 'PI = 206486', 'PI = 186283', 'PI = 206901', 'TMP = 8752'],
    'Country': ['Turkey', 'Unknown', 'U.S', 'Spain', 'Unknown', 'Turkey', 'Australia', 'Turkey', 'Unknown'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8])
