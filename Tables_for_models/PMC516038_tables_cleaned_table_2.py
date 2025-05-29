import pandas as pd

df = pd.DataFrame({
    '': ['Neck n:30 12 %', 'Shoulder n:39 14 %', 'Upper Back n:15 9 %', 'Elbow n:22 8 %', 'Lower Back n:72 26 %', 'Wrist/Hand n:48 18 %', 'Hip/Thigh n:6 2 %', 'Knee n:20 8 %', 'Ankle/Foot n:9 3 %'],
    'Orthopedic Rehabilitation %': ['9.1', '11.4', '6.8', '13.6', '29.5', '18.2', '2.3', '6.8', '2.3'],
    'General Physical Therapy %': ['10.9', '16.9', '5.0', '7.9', '25.7', '22.8', '3.0', '5.9', '2.0'],
    'Neurological Rehabilitation %': ['15.1', '15.1', '5.8', '8.1', '28.0', '12.8', '2.3', '9.3', '3.5'],
    'Cardiopulmonary Rehabilitation %': ['6.7', '16.7', '6.6', '3.3', '30.0', '16.7', '0.0', '10.0', '10.0'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8])
