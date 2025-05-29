import pandas as pd

df = pd.DataFrame({
    'Sample name': ['VB1', 'VB2', 'S', 'ST1', 'ST2', 'VB3', 'VB4', 'FB'],
    'Collection date (2001)': ['March 20', 'April 3', 'April 18', 'May 3', 'June 19', 'August 7', 'October 15', 'October 15'],
    'Tissue description': ['Overwintered terminal vegetative buds', 'Overwintered terminal vegetative buds approximately 1 week prior to bud flush', 'Newly expanding shoots (average shoot elongation = 38 mm)', 'Shoot tips, including unexpanded leaves', 'Shoot tips, including unexpanded leaves', 'Terminal vegetative buds', 'Terminal vegetative buds', 'Inflorescence buds'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7])
