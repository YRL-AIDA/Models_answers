import pandas as pd

df = pd.DataFrame({
    'GABA sensitivity': ['Responders', 'Responders', 'Non-responders', 'Non-responders', 'Control', 'Control'],
    'Mean percentage of control Ca 2+ influx': ['110 ± 2 %', '77 ± 2 %', '121 ± 4 %', '81 ± 3 %', '169 ± 24 %', '85 ± 2 %'],
    'Number of neurones': ['3 of 18', '15 of 18', '10 of 23', '13 of 23', '28 of 49', '21 of 49'],
    'Proportion of Neurones': ['17 %', '83 %', '43 %', '57 %', '57 %', '43 %'],
}, index=[0, 1, 2, 3, 4, 5])
