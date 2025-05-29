import pandas as pd

df = pd.DataFrame({
    'The referring practitioner': ['The Family practitioner', 'By ambulance', 'Other practitioner***', 'Total'],
    '"Working hours"**': ['125 (87.5%)', '16 (11%)', '2 (1.5%)', '143 (100%)'],
    '"Out of hours"': ['22 (41.5%)', '19 (36%)', '12 (22.5%)', '53 (100%)'],
    'Total': ['147', '35', '14', '196'],
}, index=[0, 1, 2, 3])
