import pandas as pd

df = pd.DataFrame({
    'QoL items': ['Global QoL', 'Physical functioning', 'Role functioning', 'Emotional functioning', 'Cognitive functioning', 'Social functioning', 'Fatigue', 'Appetite loss', 'Dyspnoea', 'Coughing', 'Haemoptysis', 'Pain in chest', 'Pain in arm or shoulder', 'Pain in other parts'],
    'Baseline mean (standard deviation)': ['36.0 (24.7)', '47.47 (24.74)', '42.67 (35.05)', '67.67 (28.39)', '66.00 (28.66)', '42.67 (32.30)', '64.89 (25.99)', '41.33 (36.36)', '60.44 (28.16)', '58.67 (36.36)', '12.00 (18.95)', '36.00 (33.22)', '24.00 (28.09)', '25.33 (27.69)'],
    '2nd cycle mean (standard deviation)': ['55.4 (16.2)', '65.22 (20.59)', '56.52 (25.99)', '84.78 (19.57)', '76.09 (18.69)', '60.87 (26.88)', '45.89 (22.30)', '20.29 (24.08)', '39.61 (23.88)', '28.99 (30.66)', '7.25 (17.28)', '17.39 (19.77)', '13.04 (19.43)', '14.49 (22.08)'],
    'p value': ['0.01', '0.01', '0.03', '<0.01', '0.08', '0.01', '<0.01', '0.01', '<0.01', '<0.01', '0.21', '0.04', '0.03', '0.02'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
