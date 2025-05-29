import pandas as pd

df = pd.DataFrame({
    'response': ['complete', 'partial', 'no change', 'progressive'],
    'group I': ['0/6', '0/6', '0/6', '6/6'],
    'group II': ['0/6', '0/6', '0/6', '6/6'],
    'group III': ['0/6', '1/6', '0/6', '5/6'],
    'group IV': ['0/6', '1/6', '0/6', '5/6'],
    'group V': ['2/6', '1/6', '1/6', '2/6'],
}, index=[0, 1, 2, 3])
