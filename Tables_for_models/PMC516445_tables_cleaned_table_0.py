import pandas as pd

df = pd.DataFrame({
    'Metal Ion %': ['Al(III)', 'Fe(III)', 'Cu(II)', 'Cd(II)', 'Pb(II)', 'Zn(II)'],
    'Concentration of Metal Ions (ng/ml)': ['80.1', '32.1', '145.3', '0.05', '0.03', '20.4'],
    'Metal Ion Adsorption (μg/g)': ['40.3 ± 0.1', '10.8 ± 0.2', '28.3 ± 0.2', 'nd', 'nd', '1.5 ± 0.1'],
    'Adsorbed Metal Ions (%)': ['98.9', '54.3', '35.1', '-', '-', '28.6'],
}, index=[0, 1, 2, 3, 4, 5])
