import pandas as pd

df = pd.DataFrame({
    'Patients G.C. (no. 1)': ['G.C. (no. 1)', 'G.L. (no. 2)', 'P.A.M. (no. 3)', 'T.N. (no. 5)', 'P.I.M. (no. 4)', 'PA.M. (no. 3)', 'S.G. (no. 6)', 'S.G. (no. 6)', 'R.L. (no. 7)', 'G.D. (no. 8)'],
    'i': ['i', 'i', 'i', 'm', 'm', 'm', 'm', 'm', 'm', 'm'],
    '6': ['6.9', '9', '6', '5.6', '12', '7', '6.4', '6.7', '4', '4'],
    'Isotope 99m Tc-HMPAO': ['99m Tc-HMPAO', '99m Tc-HMPAO', '111 In-Oxine', '99m Tc-HMPAO', '99m Tc-HMPAO', '111 In-Oxine', '99m Tc-HMPAO', '111 In-Oxine', '99m Tc-HMPAO', '99m Tc-HMPAO'],
    'Max uptake (%) * 0.22': ['0.05', '0.05', '0.42', '1.75', '0.53', '3.14', '0.39', '1.88', '0.95', '1.02'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
