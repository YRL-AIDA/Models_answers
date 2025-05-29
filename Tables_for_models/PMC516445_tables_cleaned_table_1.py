import pandas as pd

df = pd.DataFrame({
    'Metal Ion %': ['Al(III)', 'Fe(III)', 'Cu(II)', 'Zn(II)'],
    'Concentration of Metal Ions (ng/ml)': ['18.96', '0.05', '0.82', '1.26'],
    'Metal Ion Adsorption (μg/g)': ['9.46 ± 0.1', '-', '0.16 ± 0.01', '0.44 ± 0.01'],
    'Adsorbed Metal Ions (%)': ['99.7', '-', '40.0', '69.8'],
}, index=[0, 1, 2, 3])
