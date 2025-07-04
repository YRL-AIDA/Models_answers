import pandas as pd

df = pd.DataFrame({
    'Protease': ['Cathepsin B 1', 'Cathepsin C', 'Cathepsin D/E', 'Cathepsin H', 'Cathepsin J', 'Cathepsin L', 'BLT esterase', 'Suc-FLF-SBz esterase', 'Suc-AAPFSBZ esterase'],
    'XS52 DC': ['133 ± 39 2', '34 ± 7', '34 ± 6', '2.8 ± 0.8', '26 ± 0.3', '14 ± 0.6', '25,000 ± 400', '1,900,000 ± 61,000', '433,000 ± 2,900'],
    'Splenic DC': ['123 ± 3.3', '16 ± 4', '30 ± 14', '3.5 ± 0.7', '0.7 ± 0.3', '26 ± 11', '58,000 ± 4,000', '310,000 ± 10,800', '134,000 ± 7,300'],
    'Bone Marrow DC': ['121 ± 3.3', '0.4 ± 0.1', '22 ± 2', '1 ± 0.2', '3.0 ± 0.1', '19 ± 0.6', '21,300 ± 100', '1,150,000 ± 10,200', '360,000 ± 6,100'],
    'BW5147 Thymoma Cells': ['1.5 ± 0.08', '<0.01', '1.6 ± 0.1', '0.9 ± 0.2', '0.2 ± 0.09', '0.6 ± 0.08', '<100', '12,000 ± 100', '3,400 ± 600'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8])
