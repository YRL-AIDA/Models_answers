import pandas as pd

df = pd.DataFrame({
    'Authors': ['Bohen et al . (2003)', 'Sorlie et al. (2003)', 'Garber et al . (2001)', 'Alizadeh et al .(2000)', 'Gasch et al. (2000)', 'Ogawa et al. (2000)', 'Ferrea et al. (1999)', 'Spellman et al . (1998).'],
    'Ref': ['[21]', '[22]', '[23]', '[24]', '[25]', '[26]', '[27]', '[28]'],
    'Organism': ['human', 'human', 'human', 'human', 'yeast', 'yeast', 'yeast', 'yeast'],
    'Number of genes': ['16523', '552', '918', '4026', '6153', '6013', '5769', '6178'],
    'Number of experimental conditions': ['16', '122', '73', '96', '178', '8', '4', '77'],
    'Missing Values percentage (%)': ['7.6', '6.2', '2.4', '5.3', '3.0', '0.8', '10.6', '5.9'],
    'genes with missing values (%)': ['63.6', '94.7', '72.7', '78.8', '87.7', '3.8', '30.9', '91.8'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7])
