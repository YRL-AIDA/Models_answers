import pandas as pd

df = pd.DataFrame({
    '': ['EC-CDSs predicted', 'True positive', 'False positive', 'False negative', 'Sensitivity', 'Specificity', 'Inconsistence rate in T.P.'],
    'Compared to originally annotated EC-CDSs': ['1894', '1204', '690', '14', '98.9%', '63.6%', '0.08%'],
    'Compared to all originally annotated CDSs': ['1894', '1813', '55', 'NA', 'NA', '97.1%', '3.32%'],
}, index=[0, 1, 2, 3, 4, 5, 6])
