headers: (0,0);(0,1);(0,2);(0,3);(0,4)

import pandas as pd

df = pd.DataFrame({
    'Explanatory variable 1': ['Low parasite density', 'High parasite density', 'No parasitaemia', 'Age (years)', 'Age squared'],
    'Crude odds ratio (95% Cl)': ['3.98 (1.276–13.095)', '3.17 (0.601–16.692)', '1', '0.86 (0.789 – 0.94)', '0.99 (0.99 – 0.998)'],
    'p-value': ['0.02', '0.038', '0.17', '0.369', '', '', '0.001', '0.002', '0.007', '0.007'],
    'Adjusted odds ratio (95% Cl)': ['4.38 (1.10–17.69)', '2.43 (0.35–16.73)', '1', '0.51 (0.332–0.772)', '1.03 (1.007–1.047)'],
    'p-value': ['0.02', '0.038', '0.17', '0.369', '', '', '0.001', '0.002', '0.007', '0.007'],
}, index=[0, 1, 2, 3, 4])
