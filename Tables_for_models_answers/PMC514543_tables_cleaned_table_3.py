headers: (0,0);(0,1);(0,2);(0,3);(0,4);(0,5);(0,6)

import pandas as pd

df = pd.DataFrame({
    'Marker System': ['ISSR', 'RAPD', 'ISSR + RAPD'],
    'No. Of primers': ['18', '10', '28'],
    '% Polymorphism': ['93.64', '95.83', '94.05'],
    'Average No. Of bands/Primer': ['9.61', '9.7', '9.65'],
    'H av': ['0.330', '0.346', '0.338'],
    '(H av )p': ['0.354', '0.361', '0.359'],
    'MI': ['3.17', '3.35', '-'],
}, index=[0, 1, 2])
