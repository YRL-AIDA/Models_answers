import pandas as pd

df = pd.DataFrame({
    'Terrestrial vertebrates': ["Stem pig duplicates (Branch '1' in Figure 5)", 'Remaining branches', 'Totals'],
    'Non-synonymous substitutions': ['23', '598', '621'],
    'Synonymous substitutions': ['9', '1449', '1458'],
    'Totals': ['32', '2047', '2079'],
}, index=[0, 1, 2])
