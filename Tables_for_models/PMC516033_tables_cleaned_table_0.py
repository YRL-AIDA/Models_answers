import pandas as pd

df = pd.DataFrame({
    'Pre-operative diagnosis': ["Barrett's T3 N0 ACA", "Barrett's T3 N0 ACA", "Barrett's T3 N0 ACA", "Barrett's HGD", "Barrett's HGD", "Barrett's T3 N0 ACA", "Barrett's T2 N0 ACA", "Barrett's T2 N0 ACA"],
    'Sex': ['F', 'F', 'F', 'M', 'M', 'M', 'M', 'M'],
    'Age': ['58', '64', '64', '64', '72', '69', '78', '80'],
    'F/u diagnosis': ["Barrett's T2 N1", "Barrett's LGD", "Barrett's LGD", "Barrett's LGD", "Barrett's Metaplasia", "Barrett's T1 N0", "Barrett's metaplasia", 'BE+HGD'],
    'Time to F/U': ['7 mos', '42 mos', '42 mos', '47 mos', '90 mos', '18 mos', '17 mos', '88 mos'],
    'Tx': ['Surgery', 'PPI', 'PPI', 'PPI', 'PPI', 'Surgery', 'PPI', 'PDT'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7])
