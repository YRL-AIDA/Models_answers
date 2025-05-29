headers: (0,0);(0,1)

import pandas as pd

df = pd.DataFrame({
    'Response': ['Complete Response', 'Partial Response', 'Overall Response Rate (CR+PR)', 'Stable disease', 'Tumor control rate (CR+PR+SD)', 'Progressive disease'],
    'No.(%)': ['4 (11)', '7 (20)', '11 (31)', '15 (43)', '26 (74)', '9 (26)'],
}, index=[0, 1, 2, 3, 4, 5])
