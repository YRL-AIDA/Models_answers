import pandas as pd

df = pd.DataFrame({
    '': ['Patient sex (ref: male)', '1–4 years', '5–14', '15–24', '25–44', '45–64', '65–74', '75+', 'Moderately accessible', 'Remote/very remote', 'Concession health care card holder', 'Each extra health problem'],
    'Partial coefficient (a) (95%CI)': ['0.0 (-0.6;0.5)', '2.2 (1.5;2.9)', '-0.2 (-0.8;0.4)', '0.5 (-0.1;1.2)', '2.2 (1.5;3.0)', '1.9 (1.1;2.8)', '2.0 (0.9;3.1)', '2.7 (1.4;4.1)', '-1.0 (-2.1;0.2)', '-2.3 (-3.1;-1.5)', '2.6 (1.8;3.3)', '1.6 (1.3;1.8)'],
    'p-value': ['0.88', '<.001', '0.46', '0.08', '<.001', '<.001', '<.001', '<.001', '0.12', '<.001', '<.001', '<.001'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
