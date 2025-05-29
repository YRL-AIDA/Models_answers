import pandas as pd

df = pd.DataFrame({
    'Promoter': ['BLVp', 'CMVp'],
    'D17+Tax': ['115 ± 7', '96 ± 5'],
    'D17+BLV': ['1226 ± 15', '130 ± 23'],
    'D17+Tax+BLV': ['2038 ± 202', '118 ± 14'],
}, index=[0, 1])
