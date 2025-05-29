headers: (0,0);(0,1);(0,2);(0,3);(0,4);(0,5);(0,6)

import pandas as pd

df = pd.DataFrame({
    'Template': ['gDNA', 'MDA product'],
    'Original number of samples': ['2,950', '86'],
    'Number of excluded samples': ['169', '9'],
    'Exclusion rate': ['5.7', '10.5'],
    'Number of attempted genotypes': ['959,445', '26,565'],
    'Number of failed genotypes': ['590', '52'],
    'Genotype failure rate': ['0.06', '0.2'],
}, index=[0, 1])
