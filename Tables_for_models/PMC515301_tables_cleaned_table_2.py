import pandas as pd

df = pd.DataFrame({
    'GENE': [' UBQ ', ' TUA ', ' 18S ', ' ACT2 ', ' UBQ-L ', ' EF1β ', ' TUB ', ' ACT11 ', ' EIF4B-L ', ' CYP '],
    'MEAN a': ['15.8', '28.9', '14.0', '17.3', '19.8', '25.1', '17.7', '22.8', '20.6', '19.2'],
    'F b': ['1.42', '1.33', '4.72**', '1.29', '1.97', '3.76**', '4.45*', '1.01', '11.44**', '7.35**'],
    'MSE-ANOVA c': ['0.53', '1.56', '0.58', '1.25', '1.57', '1.87', '2.7', '5.71', '3.22', '5.14'],
    'CV (%) d': ['3.4', '5.4', '4.1', '7.2', '7.9', '7.5', '15.3', '25.0', '15.6', '26.8'],
    'SLOPE e': ['0.11', '0.10', '0.20', '0.16', '0.17', '0.28', '0.37', '0.24', '0.52', '0.67'],
    'INTERCEPT': ['15.3', '28.7', '13.2', '16.6', '19.1', '23.8', '16', '21.7', '18.2', '16.2'],
    'R 2': ['0.56', '0.28', '0.52', '0.57', '0.35', '0.6', '0.63', '0.37', '0.68', '0.84'],
    'MS-REG f': ['0.49', '1.65', '0.38', '1.14', '1.62', '1.41', '1.92', '5.29', '1.79', '2.66'],
    'STABILITY INDEX g': ['0.37', '0.54', '0.83', '1.16', '1.35', '2.09', '5.64', '6.01', '8.13', '17.94'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
