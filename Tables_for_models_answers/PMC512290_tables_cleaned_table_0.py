headers: (0,0);(0,1)

import pandas as pd

df = pd.DataFrame({
    ' Characteristic ': ['< 60 years', '> 60 years', 'Male', 'Female', 'Larynx', 'Tongue', 'Skin and mucosa', 'Differentiated (G1)', 'Poorly differentiated (G2, G3)', 'Well defined (1 + 2)', 'No distinct border (3)', 'Diffuse invasion (4a + 4b)'],
    ' Number of cases ': ['27', '51', '54', '24', '26', '8', '44', '39', '39', '18', '43', '17'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
