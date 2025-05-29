import pandas as pd

df = pd.DataFrame({
    'Risk': ['Uniform, spatially random', 'Uniform, spatially correlated', 'Heterogeneous, spatially correlated'],
    'No': ['I', 'II', 'III'],
    'Yes': ['IV', 'V', 'VI'],
}, index=[0, 1, 2])
