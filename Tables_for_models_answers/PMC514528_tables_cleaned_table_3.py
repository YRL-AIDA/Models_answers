headers: (0,0);(0,1);(0,2);(0,3);(1,3);(1,4)

import pandas as pd

df = pd.DataFrame({
    'Gene name': ['hMLH1', 'TP53', 'HSP-70 kD 1B', 'HSP-110', 'IL-18', 'IL-8', 'IL-15', 'Granulysin', 'Caspase 2'],
    'GENBANK NUMBER': ['NM_000249', 'NM_000546', 'NM_005346', 'NM_014278', 'NM_001562', 'NM_000584', 'NM_000585', 'NM_006433', 'NM_001224'],
    'Chemistry (Applied Biosystems, Warrington, UK)': ['High-Capacity cDNA Archive Kit + TaqMan Universal PCR Master Mix (with AmpErase UNG)', 'TaqMan ® EZ-RT-PCR Kit', 'TaqMan ® EZ-RT-PCR Kit', 'TaqMan ® EZ-RT-PCR Kit', 'TaqMan ® EZ-RT-PCR Kit', 'TaqMan ® EZ-RT-PCR Kit', 'High-Capacity cDNA Archive Kit + TaqMan Universal PCR Master Mix (with AmpErase UNG)', 'TaqMan ® EZ-RT-PCR Kit', 'TaqMan ® EZ-RT-PCR Kit'],
    'MSS': ['12', '26', '26', '26', '24', '26', '12', '26', '21'],
    'MSI-H': ['16', '27', '28', '28', '28', '28', '16', '27', '18'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8])
