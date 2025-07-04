headers: (0,0);(0,2);(0,3);(1,0);(1,1)

import pandas as pd

df = pd.DataFrame({
    '8': ['', '13', '', '24', ''],
    'fwd': ['rev', 'fwd', 'rev', 'fwd', 'rev'],
    "Outer PCR primer pairs 5'-AACATCCTCCTCGCCAAGGGT": ["5'-TGCTCTCCTGACTGT GCCTGAGTAGACTCA", "5'-AACATCCTCCTCGCCAAGGGT", "5'-TGCTCTCCTGACTGT GCCTGAGTAGACTCA", "5'-CGCAAGTGAGCCAGCCACTGC", "5'-CTGGACCGCAGGAATCT GGAATCACATGCTATGGG"],
    "Inner PCR primer pairs 5'-ATATGAACTGGCAGTAGGCAC": ["5'-TTACCCTTGGGGGCCAACCGA", "5'-AGCCTGTGCCTATTCAACTGA", "5'-GCCTCCCGGCAGAAGGAATAC", "5'-CAGCCAGCTCAGGCCATCCCT", "5'-CCAGGCCTGTGAGAAGGCTGA"],
}, index=[0, 1, 2, 3, 4])
