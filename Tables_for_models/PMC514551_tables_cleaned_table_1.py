import pandas as pd

df = pd.DataFrame({
    'Immunohistochemical postivity score': ['0', '', '1', '', '2', '', '3', ''],
    'Epithelium type': ['N', 'H', 'N', 'H', 'N', 'H', 'N', 'H'],
    'FD/GM cases/total number*': ['4/14', '3/14', '0/14', '1/14', '8/14', '8/14', '2/14', '2/14'],
    'DCIS cases/total number*': ['0/8', '0/4', '6/8', '1/4', '1/8', '2/4', '1/8', '1/4'],
    'IC cases/total number*': ['11/37', '16/22', '16/37', '10/22', '9/37', '4/22', '1/37', '2/22'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7])
