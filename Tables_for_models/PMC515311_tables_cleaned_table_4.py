import pandas as pd

df = pd.DataFrame({
    'Clinical scenario': ['60-year-old woman with hypertension and high cholesterol', '', '', '', '50-year-old man without other CHD risk factors', '', '', '', '40-year-old woman who smokes', '', '', '', '80-year-old man with high cholesterol', '', '', ''],
    'Pre-test 10-year CHD risk estimate*': ['15%', '', '', '', '6%', '', '', '', '3%', '', '', '', '26%', '', '', ''],
    'CAC score category': ['0:', '1–100:', '101–400:', '>400:', '0:', '1–100:', '101–400:', '>400:', '0:', '1–100:', '101–400:', '>400:', '0:', '1–100:', '101–400:', '>400:'],
    'Proportion of CAC scores falling within the given category†': ['0.47', '0.36', '0.12', '0.05', '0.59', '0.31', '0.07', '0.03', '0.89', '0.10', '0.01', '0.00', '0.05', '0.25', '0.30', '0.40'],
    'Conservative§': ['9%', '15%', '25%', '34%', '4%', '7%', '11%', '16%', '2%', '4%', '7%', '10%', '9%', '15%', '26%', '35%'],
    'Optimistic§': ['6%', '13%', '31%', '51%', '3%', '6%', '15%', '27%', '2%', '5%', '12%', '22%', '5%', '10%', '23%', '39%'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
