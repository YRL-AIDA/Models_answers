import pandas as pd

df = pd.DataFrame({
    'Donor': ['7', '13', '14'],
    'Age (Yrs)': ['23', '22', '54'],
    'Gender': ['Female', 'Female', 'Male'],
    'Race': ['Cauc', 'Cauc', 'Cauc'],
    'Baseline': ['10.4', '10.0', '9.5'],
    'Apheresis Day': ['12.3', '11.2', '12.0'],
    '10 Days Post-Apheresis': ['11.1', '11.1', '10.5'],
    'Enlargement 10 Days Post-Apheresis': ['0.7', '1.1', '1.0'],
}, index=[0, 1, 2])
