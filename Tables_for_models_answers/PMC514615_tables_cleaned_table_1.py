headers: (0,0);(0,1);(0,2);(0,3);(0,4);(0,5);(0,6);(0,7);(0,8);(0,9);(0,10)

import pandas as pd

df = pd.DataFrame({
    '': ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
    'Author Year': ['Swanson 1986 [7]', 'Zamboni 1990 [8]', 'Zamboni 1990 [8]', 'Zamboni 1990 [8]', 'Lee 1992 [9]', 'Sarker 1992 [10]', 'Sato 1995 [11]', 'Shim 2000 [12]', 'Sata 2004 present case'],
    'Age/sex': ['76 M', '62 M', '66 M', '51 M', '86 M', '53 F', '74 M', '54 M', '57 M'],
    'Clinical Manifestations': ['Abdominal pain, anorexia, weight loss', 'jaundice, weight loss', 'jaundice, abdominal pain', 'jaundice, weight loss, abdominal pain', 'jaundice, recurrent pancreatitis', 'jaundice, weight loss, back pain', 'jaundice', 'jaundice', 'GI Tract bleeding'],
    'Size (mm)': ['15', '25', '20', '30', '?', '35', '35', '30', '30'],
    'Morphology': ['ulceration', 'polypoid', 'ulceration', 'soft fungating mass', 'polypoid', 'mass with small ulceration', 'polypoid', 'ulceration', 'mass with ulceration'],
    'Location': ['adjacent to the ampulla*', 'the papilla of Vater', 'the papilla of Vater', 'the papilla of Vater', 'Peri ampullary', 'the papilla of Vater', 'the papilla of Vater', 'the papilla of Vater', 'Peri ampullary'],
    'Metastasis': ['LN, liver', 'LN', 'LN', 'LN', '?', 'LN', '?', 'liver', '-'],
    'Surgery': ['biospy', 'PD', 'PD', 'PD', '-', 'PD', 'PPPD', 'PD', 'Local resection'],
    'Chemotherapy': ['5-FU, doxorubicin, mitomycin', '-', '-', '-', '-', '5-FU, TNF, interferon', '-', 'cisplatin, etoposide, radiation', '5-FU leucovorin'],
    'Prognosis (month)': ['Dead (1.5)', 'Dead (7)', 'Dead (6)', 'Dead (17)', '(>5)', 'Recurrence + (>18)', '?', 'Dead (8)', 'disease free (>48)'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8])
