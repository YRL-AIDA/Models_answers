import pandas as pd

df = pd.DataFrame({
    '': ['Beta-blockers', 'Calcium channel blockers', 'Nitrates', 'ACE-inhibitors', 'Aminophylline'],
    'Exercise': ['↓', '↓', '↓', '↔', '↓↔'],
    'Dipyridamole': ['↓', '↓', '↓', '↔', '↓↓'],
    'Dobutamine': ['↓↓', '↓↔', '↓↔', '↔', '↔'],
}, index=[0, 1, 2, 3, 4])
