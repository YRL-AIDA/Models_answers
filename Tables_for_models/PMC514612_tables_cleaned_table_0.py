import pandas as pd

df = pd.DataFrame({
    'Genotyping Platform': ['TaqMan', 'TaqMan', 'BeadArray', 'Invader'],
    'Site of MDA production': ['MSI', 'In-house', 'MSI', 'MSI'],
    'Number of SNPs': ['95', '2', '345', '13'],
    'Number of non-excluded samples': ['88', '448', '77', '88'],
    'Genotype Concordance Rate (%) gDNA and MDA product template': ['99.71', '99.4', '98.8', '99.9'],
    'gDNA template': ['2.4', '0.7', '0.06', '0.9'],
    'MDA product template': ['4.0', '1.9', '0.2', '2.6'],
}, index=[0, 1, 2, 3])
