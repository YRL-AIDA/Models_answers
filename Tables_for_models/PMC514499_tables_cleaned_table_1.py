import pandas as pd

df = pd.DataFrame({
    'Risk': ['Exercise capacity', 'Contractile reserve', 'Pulmonary hypertension', 'Right ventricular dysfunction', 'Mitral regurgitation'],
    'Low (5–10% year)': ['≥ 8–10 min', 'yes', '<45 mmHg', 'no', '↓ or ='],
    'High (≥ 25–30% year)': ['<8 min', 'no', '>45 mmHg', 'yes', '↑↑'],
}, index=[0, 1, 2, 3, 4])
