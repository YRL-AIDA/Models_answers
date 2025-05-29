import pandas as pd

df = pd.DataFrame({
    'Authors': ['Donner et al. [8]', 'Simpson et al. [9]', 'Isaakidis and Ioannidis [11]', 'Puffer et al. [10]', 'Eldridge et al. [12]', 'Varnell et al. [13]'],
    'Source of trials': ['16 non-therapeutic intervention trials', '21 trials from American Journal of Public Health and Preventive Medicine', '51 trials in Sub-Saharan Africa', '36 trials in British Medical Journal , Lancet , and New England Journal of Medicine', '152 trials in primary health care', '60 trials in American Journal of Public Health and Preventive Medicine'],
    'Years': ['1979 – 1989', '1990 – 1993', '1973 – 2001 (half post 1995)', '1997 – 2002', '1997 – 2000', '1998 – 2002'],
    'Clustering allowed for in sample size': ['<20%', '19%', '20%', '56%', '9%', '20%'],
    'Clustering allowed for in analysis': ['<50%', '57%', '37%', '92% a', '59%', '54% (all analyses) + 25% (some analyses only)'],
}, index=[0, 1, 2, 3, 4, 5])
