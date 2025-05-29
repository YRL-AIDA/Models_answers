import pandas as pd

df = pd.DataFrame({
    'Temperature': ['+2oC', 'Normal', '-2oC'],
    'Mosquitoes': ['47550.3', '41449.9', '36199'],
}, index=[0, 1, 2])
