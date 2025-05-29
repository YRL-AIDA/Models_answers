headers: (0,0);(0,1);(0,2);(0,3);(0,4);(0,5);(0,6);(0,7)

import pandas as pd

df = pd.DataFrame({
    'No:': ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
    'Age': ['52', '66', '60', '48', '36', '56', '71', '52', '21'],
    'Sex': ['Female', 'Male', 'Male', 'Male', 'Female', 'Female', 'Female', 'Male', 'Female'],
    'Lesion': ['Left lower eyelid', 'Left lower eyelid', 'Right lower eyelid', 'Right lower eyelid', 'Inner right canthus', 'Left lower eyelid', 'Right lower eyelid', 'Left inner canthus', 'Right inner canthus'],
    'Size of defect (mm)': ['20 × 5', '38 × 12', '28 × 8', '26 × 10', '40 × 10', '22 × 8', '45 × 10', '42 × 15', '50 × 15'],
    'Flap type': ['Mustardé', 'Mustardé', 'Mustardé', 'Mustardé', 'Tri-lobed flap', 'Bi-lobed flap', 'Tri-lobed flap', 'Forehead flap', 'Forehead flap'],
    'Pathology': ['Basal cell Ca', 'Basal cell Ca', 'Basal cell Ca', 'Basal cell Ca', 'Basal cell Ca', 'Basal cell Ca', 'Basal cell Ca', 'Basal cell Ca', 'Basal cell Ca'],
    'Complication': ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8])
