headers: (0,0);(0,1);(0,2);(0,3)

import pandas as pd

df = pd.DataFrame({
    'Variable': ['Maternal age', 'Parity', 'Gestational age at admission', 'Gestational age at delivery', 'Latency (Mean ± SD)', 'C/S rate for fetal distress', 'Birth weight (mean)'],
    'AFI<5 (n = 26)': ['25,1 ± 5.2', '3 ± 1,5', '31.5 ± 2.00', '32.6 ± 4.0', '7.6 ± 4.0', '6(%23)', '2120 gr'],
    'AFI ≥ 5 (n = 69)': ['26.3 ± 4.9', '2.4 ± 1.2', '33.5 ± 1.8', '34.5 ± 3.7', '6.6 ± 5.2', '2(28%)', '2445 gr'],
    'Statistical significance': ['Ns', 'Ns', 'Ns', 'Ns', 'Ns', 'P = 0.001, s', 'Ns'],
}, index=[0, 1, 2, 3, 4, 5, 6])
