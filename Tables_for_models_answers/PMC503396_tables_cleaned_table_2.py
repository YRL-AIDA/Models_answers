headers: (0,0);(0,1);(0,2);(0,3);(0,4)

import pandas as pd

df = pd.DataFrame({
    'Factor*': ["I don't enjoy the trach/vent population", 'I want to enter general pediatrics', "I don't enjoy certain pulmonary patients", 'There are too many chronic patients', 'I want to enter another fellowship', "I don't know enough about it to decide", 'Not enough pulmonary patient experience', "I don't enjoy the BPD + population", "I don't think pulmonary is very interesting", 'Some of the pulmonary patients scare me', "I can't afford being a fellow", 'The pulmonologists work too hard', "I don't enjoy the cystic fibrosis population", 'Too few pulmonary job openings', "I don't enjoy the asthma population", "Pulmonologists don't earn enough money", 'Poor experiences with pulmonary faculty'],
    '1992 Score': ['2.0 ± 1.1', '1.9 ± 1.2', '1.6 ± 1.1', '1.5 ± 1.1', '1.5 ± 1.2', '1.5 ± 1.1', '1.4 ± 1.1', '1.2 ± 1.0', '0.9 ± 0.9', '0.7 ± 0.8', '0.7 ± 1.1', '0.4 ± 0.6', '0.3 ± 0.6', '0.3 ± 0.5', '0.2 ± 0.5', '0.2 ± 0.5', '0.2 ± 0.4'],
    '1992 Rank': ['1', '2', '3', '4', '4', '4', '7', '8', '9', '10', '10', '12', '13', '13', '15', '15', '15'],
    '2002 Score': ['1.9 ± 1.3', '1.8 ± 1.3', '1.2 ± 1.1', '1.5 ± 1.1', '1.2 ± 1.3', '1.0 ± 1.1', '0.6 ± 0.9#', '1.2 ± 1.1', '0.6 ± 0.8', '0.8 ± 1.0', '0.4 ± 0.8', '0.4 ± 0.7', '0.6 ± 0.9', '0.0 ± 0.2#', '0.4 ± 0.8', '0.1 ± 0.4', '0.3 ± 0.8'],
    '2002 Rank': ['1', '2', '4', '3', '4', '7', '9', '4', '9', '8', '12', '12', '9', '17', '12', '16', '15'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
