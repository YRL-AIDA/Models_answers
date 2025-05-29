import pandas as pd

df = pd.DataFrame({
    'Topic covered': ['Mother-to-infant HIV transmission', 'Confidentiality', 'Right to refuse', 'Consequences of refusal to test', 'Social risk', 'Benefits of HIV testing', 'Meaning of signature', 'Right to consult', '80% coverage in sessions'],
    'N': ['30', '40', '30', '38', '29', '39', '12', '22', '2', '9', '30', '39', '21', '36', '0', '14', '9', '27'],
    '%': ['100', '100', '100', '95', '97', '98', '40', '55', '7', '23', '100', '98', '70', '90', '0', '35', '30', '68'],
    'N': ['30', '40', '30', '38', '29', '39', '12', '22', '2', '9', '30', '39', '21', '36', '0', '14', '9', '27'],
    '%': ['100', '100', '100', '95', '97', '98', '40', '55', '7', '23', '100', '98', '70', '90', '0', '35', '30', '68'],
    'Chi square χ 2 statistic and significance level': ['___', '0.2', '0.0', '1.4', '4.0*', '0.0', '6.8**', '12.6***', '13.4***'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8])
