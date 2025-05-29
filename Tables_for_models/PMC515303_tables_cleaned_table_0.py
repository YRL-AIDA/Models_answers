import pandas as pd

df = pd.DataFrame({
    'Laboratory test': ['Hemoglobin', 'White cell count', 'Band count', 'Platelets', 'Sodium', 'Potassium', 'Chloride', 'Bicarbonate', 'Glucose', 'Magnesium', 'Osmolality', 'Urea', 'Creatinine', 'Lactate', 'Serum ketones', 'Anion gap', 'Osmolar gap'],
    'Pre-dialysis Value': ['96', '25.8', '3.1', '603', '132', '3.1', '107', '2', '6.3', '0.88', '330', '46.7', '537', '0.6', '2+', '23', '14.5'],
    'Post-dialysis Values': ['78', '16.1', '-', '486', '132', '1.8', '93', '19', '9.0', '0.57', '-', '13.7', '-', '1.2', '-', '20', '-'],
    'Reference range': ['137–180 g/L', '4.0–11.0 × 10 9 /L', '0.0–1.3 × 10 9 /L', '150–400 × 10 9 /L', '133–145 mmol/L', '3.5–5.0 mmol/L', '98–111 mmol/L', '21–31 mmol/L', '3.6–11.1 mmol/L', '0.65–1.15 mmol/L', '280–300 mosmol/kg', '3.0–7.6 mmol/L', '61–111 μmol/L', '< 2.0 mmol/L', 'Undetected', '12–14', '0–10'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
