import pandas as pd

df = pd.DataFrame({
    'Laurasiatheria subtree': ["Stem pig duplicates (Branch '1' in Figure 5)", 'Remaining branches', 'Totals'],
    'Non-synonymous substitutions': ['23', '232', '255'],
    'Synonymous substitutions': ['9', '258', '267'],
    'Totals': ['32', '490', '522'],
}, index=[0, 1, 2])
