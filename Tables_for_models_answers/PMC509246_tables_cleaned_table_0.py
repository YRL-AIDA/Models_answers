headers: (0,0);(0,1);(0,2);(0,3);(0,4);(0,5);(0,6)

import pandas as pd

df = pd.DataFrame({
    'Code': ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P11', 'P12', 'P13', 'P14', 'P15', 'P16', 'P17', 'P18', 'P19', 'P20', 'P21'],
    'Age (years)': ['67', '73', '84', '83', '81', '76', '75', '60', '79', '67', '76', '80', '53', '71', '69', '77', '78', '80', '71', '71', '82'],
    'Sex': ['F', 'M', 'M', 'F', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'M', 'M', 'M', 'M', 'F', 'M', 'M', 'M', 'F', 'F'],
    'Marital Status': ['Widowed', 'Married', 'Widowed', 'Married', 'Married', 'Married', 'Divorced', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married'],
    'Employment Status': ['Retired', 'Retired', 'Retired', 'Retired', 'Retired', 'Retired', 'Retired', 'Working', 'Retired', 'Retired', 'Retired', 'Retired', 'Working', 'Retired', 'Retired', 'Retired', 'Retired', 'Retired', 'Working', 'Retired', 'Retired'],
    'Years on Warfarin': ['5', '10', '5', '4', '1', '3', '2', '3', '5', '2', '5', '2', '8', '3', '4', '5', '1', '10', '7', '6', '5'],
    'INR in Range?': ['Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
