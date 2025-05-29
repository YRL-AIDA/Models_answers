headers: (0,0);(0,1);(0,2);(0,3)

import pandas as pd

df = pd.DataFrame({
    'Sequence': ['PseudoBase', '7 HIVRT', '14 tRNAs', 'HDV', 'ag-HDV', 'TYMV', 'TMV (up)', 'STNV'],
    'Length': ['variable', '35', '71–82', '87', '91', '86', '85', '252'],
    'BP': ['variable', '11', '18–19', '32', '25', '24', '25', '69'],
    'Reference': ['[14]', '[34]', '', '[32]', '[32]', '[35]', '[36]', 'GenBank:M64479'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7])
