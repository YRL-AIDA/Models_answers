import pandas as pd

df = pd.DataFrame({
    'Genotypes': ['WT', 'AS--', 'AS-', 'S++', 'A'],
    'Mean diff. in capsule number': ['18.04', '40.36', '23.14', '12.64', '32.25'],
    '% Mean diff. in capsule number': ['54.18', '91.35', '68.14', '35.47', '65.58'],
    'P': ['<0.0001', '<0.0001', '<0.0001', '<0.0001', '<0.0001'],
    'TPI levels': ['High', 'Low', 'Intermediate', 'High', 'No TPI'],
}, index=[0, 1, 2, 3, 4])
