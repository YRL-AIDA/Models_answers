import pandas as pd

df = pd.DataFrame({
    '': ['Larvae', 'Pupae', 'Total'],
    'Stage duration (days)': ['9.98', '1.79', '11.77'],
    'With predators': ['90.9', '73.49', '97.6'],
    'Without predators': ['79.58', '35.63', '86.85'],
    'Attributable to Predators': ['11.34', '37.86', '0.11'],
}, index=[0, 1, 2])
