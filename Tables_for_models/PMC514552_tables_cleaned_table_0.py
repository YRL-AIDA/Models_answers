import pandas as pd

df = pd.DataFrame({
    'Variable': ['Age group*', 'Total cholesterol**', 'Alcohol consumption†', 'Age group*', 'Initial insomnia‡', 'Quality of sleep ±', 'Alcohol consumption†', 'Age group*', 'Initial insomnia‡', 'Quality of sleep ±', 'Alcohol consumption†'],
    'coefficient': ['-.8', '-1.6', '-1.6', '-1.0', '1.8', '-2.1', '-1.2', '-1.1', '1.5', '-1.6', '-1.8'],
    's.e.': ['.50', '.66', '.62', '.52', '.72', '.69', '.60', '.53', '.70', '.66', '.62'],
    'p value': ['.09', '.01', '.008', '.05', '.01', '.002', '.04', '.04', '.03', '.02', '.005'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
