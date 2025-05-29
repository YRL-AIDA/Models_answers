import pandas as pd

df = pd.DataFrame({
    '': ['Female patient', '<15 years', '15–24', '25–44', '45–64', '65–74', '75+', 'Address in "highly accessible" location', 'Speaks language other than English at home.', 'Holds concession health care card'],
    'Sample n (%)': ['6,404 (59.5)', '1,360 (12.7)', '1,005 (9.4)', '2,875 (26.9)', '2,677 (25.0)', '1,274 (11.9)', '1,514 (14.1)', '8,702 (83.3)', '890 (8.3)', '4,448 (41.4)'],
    'Australian population of general practice patients (a) %': ['53.4', '19.9', '13.1', '29.7', '23.8', '7.6', '5.9', 'Not available', 'Not available', 'Not available'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
