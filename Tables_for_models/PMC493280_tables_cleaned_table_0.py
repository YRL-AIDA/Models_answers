import pandas as pd

df = pd.DataFrame({
    'No.': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21'],
    'Age': ['52', '55', '55', '75', '61', '53', '63', '65', '47', '41', '54', '52', '57', '46', '73', '55', '51', '62', '42', '62', '40'],
    'Male/female': ['f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'M', 'f', 'f'],
    'Symptoms': ['Transient ischemic attack', 'Bruit', 'Headache', 'Bruit', 'Vertigo', 'Pulsatile tinnitus', 'Vertigo', 'Amaurosis fugax', 'Amaurosis fugax, vertigo', 'Minor stroke', 'Minor stroke', 'Headache, vertigo', 'Minor stroke', 'Vertigo, bruit', 'Bruit, headache, vertigo', 'Headache', 'Headache', 'Headache', 'Transient ischemic attack', 'Transient ischemic attack', 'Headache'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
