import pandas as pd

df = pd.DataFrame({
    'Variable': ['Male', 'Female', 'Single', 'Married', 'Focal/Segmental', 'Generalized', 'Covered/Uncovered', 'Covered'],
    "Cronbach's coefficient (n 1 )": ['0.60 (27)', '0.80 (43)', '0.79 (42)', '0.75 (28)', '0.58 (18)', '0.79 (52)', '0.78 (54)', '0.67 (16)'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7])
