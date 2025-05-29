import pandas as pd

df = pd.DataFrame({
    'Model': ['Cyt b-Myo-G3PDH', 'Cyt b, Myo, G3PDH', 'Cyt b-Myo-G3PDH*', 'Cyt b, Myo, G3PDH*'],
    'Cyt b-Myo-G3PDH': ['0', '', '', ''],
    'Cyt b, Myo, G3PDH': ['241.36', '0', '', ''],
    'Cyt b-Myo-G3PDH*': ['-5421.2', '-5662.56', '0', ''],
    'Cyt b, Myo, G3PDH*': ['-5125.22', '-5366.58', '295.98', '0'],
}, index=[0, 1, 2, 3])
