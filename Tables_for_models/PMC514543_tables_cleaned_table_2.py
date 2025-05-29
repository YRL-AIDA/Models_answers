import pandas as pd

df = pd.DataFrame({
    'Marker System': ['ISSR', 'RAPD', 'ISSR + RAPD'],
    'No. of primers': ['14', '22', '36'],
    '% Polymorphism': ['72', '70.12', '70.8'],
    'Average No. Of bands/Primer': ['7.14', '7.45', '7.33'],
    'H av': ['0.2145', '0.203', '0.211'],
    '(H av )p': ['0.297', '0.289', '0.298'],
    'MI': ['1.53', '1.51', '-'],
}, index=[0, 1, 2])
