headers: (0,0);(0,1);(1,1);(1,4);(1,7);(2,1);(2,2);(2,3);(2,4);(2,5);(2,6);(2,7);(2,8);(2,9)

import pandas as pd

df = pd.DataFrame({
    'Treatment': ['Control', 'TGF-β', 'IL-1β', 'IL-2', 'IL-6', 'IL-8'],
    'MT1-MMP ± SEM': ['1.00 ± 0.06', '1.00 ± 0.08', '1.00 ± 0.08', '0.52 ± 0.06', '0.96 ± 0.08', '0.80 ± 0.04', '0.58 ± 0.06', '1.12 ± 0.10', '0.70 ± 0.04', '0.75 ± 0.14', '0.59 ± 0.02', '0.70 ± 0.04', '0.56 ± 0.02', '0.85 ± 0.05', '0.64 ± 0.02', '0.45 ± 0.03', '0.75 ± 0.05', '0.92 ± 0.04'],
    'MMP-11 ± SEM': ['1.00 ± 0.14', '1.00 ± 0.10', '1.00 ± 0.08', '1.14 ± 0.08', '1.14 ± 0.06', '0.95 ± 0.08', '0.74 ± 0.04', '0.74 ± 0.06', '0.75 ± 0.08', '0.90 ± 0.08', '0.68 ± 0.05', '0.75 ± 0.04', '0.90 ± 0.02', '0.78 ± 0.08', '0.74 ± 0.06', '0.96 ± 0.04', '0.74 ± 0.05', '0.76 ± 0.03'],
    '18S rRNA ± SEM': ['1.00 ± 0.04', '1.00 ± 0.04', '1.00 ± 0.02', '1.35 ± 0.14', '1.35 ± 0.16', '1.34 ± 0.12', '1.10 ± 0.10', '1.24 ± 0.08', '1.10 ± 0.08', '0.94 ± 0.06', '0.95 ± 0.06', '0.90 ± 0.02', '0.75 ± 0.06', '1.15 ± 0.07', '1.20 ± 0.02', '0.90 ± 0.02', '1.00 ± 0.08', '0.92 ± 0.02'],
    'MT1-MMP ± SEM': ['1.00 ± 0.06', '1.00 ± 0.08', '1.00 ± 0.08', '0.52 ± 0.06', '0.96 ± 0.08', '0.80 ± 0.04', '0.58 ± 0.06', '1.12 ± 0.10', '0.70 ± 0.04', '0.75 ± 0.14', '0.59 ± 0.02', '0.70 ± 0.04', '0.56 ± 0.02', '0.85 ± 0.05', '0.64 ± 0.02', '0.45 ± 0.03', '0.75 ± 0.05', '0.92 ± 0.04'],
    'MMP-11 ± SEM': ['1.00 ± 0.14', '1.00 ± 0.10', '1.00 ± 0.08', '1.14 ± 0.08', '1.14 ± 0.06', '0.95 ± 0.08', '0.74 ± 0.04', '0.74 ± 0.06', '0.75 ± 0.08', '0.90 ± 0.08', '0.68 ± 0.05', '0.75 ± 0.04', '0.90 ± 0.02', '0.78 ± 0.08', '0.74 ± 0.06', '0.96 ± 0.04', '0.74 ± 0.05', '0.76 ± 0.03'],
    '18S rRNA ± SEM': ['1.00 ± 0.04', '1.00 ± 0.04', '1.00 ± 0.02', '1.35 ± 0.14', '1.35 ± 0.16', '1.34 ± 0.12', '1.10 ± 0.10', '1.24 ± 0.08', '1.10 ± 0.08', '0.94 ± 0.06', '0.95 ± 0.06', '0.90 ± 0.02', '0.75 ± 0.06', '1.15 ± 0.07', '1.20 ± 0.02', '0.90 ± 0.02', '1.00 ± 0.08', '0.92 ± 0.02'],
    'MT1-MMP ± SEM': ['1.00 ± 0.06', '1.00 ± 0.08', '1.00 ± 0.08', '0.52 ± 0.06', '0.96 ± 0.08', '0.80 ± 0.04', '0.58 ± 0.06', '1.12 ± 0.10', '0.70 ± 0.04', '0.75 ± 0.14', '0.59 ± 0.02', '0.70 ± 0.04', '0.56 ± 0.02', '0.85 ± 0.05', '0.64 ± 0.02', '0.45 ± 0.03', '0.75 ± 0.05', '0.92 ± 0.04'],
    'MMP-11 ± SEM': ['1.00 ± 0.14', '1.00 ± 0.10', '1.00 ± 0.08', '1.14 ± 0.08', '1.14 ± 0.06', '0.95 ± 0.08', '0.74 ± 0.04', '0.74 ± 0.06', '0.75 ± 0.08', '0.90 ± 0.08', '0.68 ± 0.05', '0.75 ± 0.04', '0.90 ± 0.02', '0.78 ± 0.08', '0.74 ± 0.06', '0.96 ± 0.04', '0.74 ± 0.05', '0.76 ± 0.03'],
    '18S rRNA ± SEM': ['1.00 ± 0.04', '1.00 ± 0.04', '1.00 ± 0.02', '1.35 ± 0.14', '1.35 ± 0.16', '1.34 ± 0.12', '1.10 ± 0.10', '1.24 ± 0.08', '1.10 ± 0.08', '0.94 ± 0.06', '0.95 ± 0.06', '0.90 ± 0.02', '0.75 ± 0.06', '1.15 ± 0.07', '1.20 ± 0.02', '0.90 ± 0.02', '1.00 ± 0.08', '0.92 ± 0.02'],
}, index=[0, 1, 2, 3, 4, 5])
