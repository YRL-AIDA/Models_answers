import pandas as pd

df = pd.DataFrame({
    'Function Categories a': ['Carbohydrate metabolism', 'Energy metabolism', 'Lipid metabolism', 'Nucleotide metabolism', 'Amino Acid metabolism', 'Other Amino Acids', 'Complex Carbohydrates', 'Complex Lipids metabolism', 'Cofactors and Vitamins', 'Sum of unique EC numbers'],
    'ECs b': ['427', '167', '126', '166', '561', '146', '184', '171', '225', '1899'],
    'KPN (735)': ['151', '60', '27', '83', '211', '49', '63', '46', '104', '567'],
    'ECO (681)': ['154', '62', '25', '82', '189', '45', '58', '38', '105', '537'],
    'STM (655)': ['147', '62', '25', '80', '189', '43', '55', '34', '107', '529'],
    'STY (445)': ['101', '46', '17', '45', '132', '26', '33', '24', '74', '349'],
    'PAO (573)': ['105', '61', '27', '66', '205', '47', '43', '31', '100', '464'],
    'YPE (585)': ['123', '58', '17', '72', '183', '41', '53', '34', '96', '476'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
