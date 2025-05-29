import pandas as pd

df = pd.DataFrame({
    'Cell line': ['AML-193', 'HL-60', 'THP-1', 'U-937'],
    'IC 50 (nM)†': ['134', '24', '19', '44'],
    'ras status': ['H- ras (12), N- ras (13)', 'H- ras (12)', 'K- ras (13) N- ras (12, 61)', 'Wild-type'],
}, index=[0, 1, 2, 3])
