import pandas as pd

df = pd.DataFrame({
    'Model': ['Cyt b-Myo-G3PDH', 'Cyt b, Myo-G3PDH', 'Cyt b-Myo, G3PDH', 'Cyt b-G3PDH, Myo', 'Cyt b, Myo, G3PDH'],
    'Cyt b-Myo-G3PDH': ['0', '', '', '', ''],
    'Cyt b, Myo-G3PDH': ['60.84', '0', '', '', ''],
    'Cyt b-Myo, G3PDH': ['118.12', '57.28', '0', '', ''],
    'Cyt b-G3PDH, Myo': ['102.26', '41.42', '-15.86', '0', ''],
    'Cyt b, Myo, G3PDH': ['241.36', '180.52', '123.24', '139.1', '0'],
}, index=[0, 1, 2, 3, 4])
