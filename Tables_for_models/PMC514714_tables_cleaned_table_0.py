import pandas as pd

df = pd.DataFrame({
    'Variable': ['Age', '<65', '65–74', '75–84', '>84', 'Male', 'Female', '1–2 days', '3–6 days', '7–13 days', '>13 days', 'Nursing home resident', 'Pneumonia Severity Index', 'I-III', 'IV', 'V', 'Malignancy', 'Chronic renal disease', 'Liver disease', 'Congestive heart failure', 'History of stroke'],
    'White n = 720*': ['', '132', '189', '255', '144', '312', '408', '63', '375', '220', '60', '148', '', '280', '296', '142', '57', '75', '9', '199', '105'],
    '%': ['', '', '18.3', '18.3', '26.3', '26.3', '35.4', '35.4', '20.0', '20.0', '43.3', '43.3', '56.6', '56.7', '8.8', '9.6', '52.2', '48.3', '30.6', '31.7', '8.4', '10.4', '21.0', '22.2', '', '', '39.0', '28.8', '41.2', '41.1', '19.8', '30.1', '8.0', '12.2', '10.6', '25.2', '1.3', '2.2', '20.0', '34.9', '14.9', '23.9'],
    'Black n = 240': ['', '44', '63', '85', '48', '104', '136', '23', '116', '76', '25', '51', '', '68', '97', '71', '28', '58', '5', '80', '55'],
    '%': ['', '', '18.3', '18.3', '26.3', '26.3', '35.4', '35.4', '20.0', '20.0', '43.3', '43.3', '56.6', '56.7', '8.8', '9.6', '52.2', '48.3', '30.6', '31.7', '8.4', '10.4', '21.0', '22.2', '', '', '39.0', '28.8', '41.2', '41.1', '19.8', '30.1', '8.0', '12.2', '10.6', '25.2', '1.3', '2.2', '20.0', '34.9', '14.9', '23.9'],
    'p-value': ['1.00', '', '', '', '', '', '', '0.663', '', '', '', '0.774', '0.001', '', '', '', '0.073', '0.000', '0.039', '0.057', '0.002'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
