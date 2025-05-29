headers: (0,0);(0,1);(0,2);(0,3);(0,4)

import pandas as pd

df = pd.DataFrame({
    'Patients': ['R.L. (no. 7)', 'G.D. (no. 8)', 'R.L. (no. 7)', 'G.D. (no. 8)'],
    'mDC × 10 6': ['4', '4', '4', '4'],
    'Administration route': ['Intradermal', 'Intradermal', 'Subcutaneous', 'Subcutaneous'],
    'Isotope': ['99m Tc-HMPAO', '99m Tc-HMPAO', '99m Tc-HMPAO', '99m Tc-HMPAO'],
    'Max uptake (%) *': ['0.95', '1.02', '0.30', '0.37'],
}, index=[0, 1, 2, 3])
