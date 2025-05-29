headers: (0,0);(0,1);(0,2);(0,3);(0,4)

import pandas as pd

df = pd.DataFrame({
    'C. elegans AADC': ['C05D2.4 ( bas-1 )', 'C05D2.3', 'C09G9.4', 'F12A10.3', 'K01C8.3 ( tdc-1 )', 'Y37D8A.23 ( unc-25 )', 'ZK289.2'],
    'C.e. cDNAs': ['+(3) a,b,c,d', '+ a,c', '+ d', '+(2) b,d', '+(2) c,d', '+(3) c,d', '+ c,d'],
    'C.e. Microarray': ['+', '-', '-', '-', '+', '+', '-'],
    'C. briggsae ortholog': ['FPC2187 (84,978 / - strand)', 'none', 'FPC4079 (~28,330 / + strand)', 'none', 'FPC0011 (663,153 / + strand)', 'FPC4030 (765,572 / - strand)', 'FPC0143 (1,747,392 / - strand)'],
    'C.b. cDNAs': ['+ a', 'NA', '-', 'NA', '+', '-', '-'],
}, index=[0, 1, 2, 3, 4, 5, 6])
