headers: (0,0);(0,1);(0,2);(0,3);(0,4)

import pandas as pd

df = pd.DataFrame({
    'Experimental design': ['Control ( n = 4 )', 'Sham (CLP) 6 hr ( n = 4 )', 'Sham (CLP) 24 hr ( n = 6 )', 'CLP 6 hr ( n = 6 )', 'CLP 24 hr ( n = 6 )', '2% Glycogen 6 hr ( n = 4 )'],
    'WT mice Total Leukocytes (× 10 6 /mL)': ['10.1 ± 1.3', '3.6 ± 0.6 *', '2.9 ± 0.7 *', '2.0 ± 0.4 *', '1.1 ± 0.3 *', '3.4 ± 0.1 *'],
    'P/I null mice Total Leukocytes (× 10 6 /mL)': ['10.3 ± 2.1', '4.5 ± 0.3 *', '4.4 ± 0.8 *', '3.4 ± 0.9 *', '3.8 ± 1.1 *', '4.4 ± 0.8 *'],
    'WT mice Neutrophils (× 10 6 /mL)': ['2.8 ± 0.7 #', '2.2 ± 0.1 #', '1.4 ± 0.3 *', '1.2 ± 0.3 *', '0.6 ± 0.2 *', '2.5 ± 0.1'],
    'P/I null mice Neutrophils (× 10 6 /mL)': ['6.7 ± 1.3', '3.8 ± 0.5', '2.3 ± 0.1 *', '2.8 ± 0.9 *', '2.8 ± 0.8 *', '3.6± 0.6'],
}, index=[0, 1, 2, 3, 4, 5])
