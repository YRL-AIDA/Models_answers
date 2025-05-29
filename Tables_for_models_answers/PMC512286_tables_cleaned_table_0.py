headers: (0,0);(0,1);(0,2)

import pandas as pd

df = pd.DataFrame({
    'Health Category': ['A A1', 'A2', 'B B1', 'B2', 'C', 'D'],
    'Description *': ['Completely healthy; no medication', 'Completely healthy; using only preventive medication', 'Functioning normally; presence of stabilised, non cardiovascular disease; absence of cardiovascular abnormalities', 'Functioning normally; using medication with cardiovascular effect, no overt cardiovascular disease other than normalized arterial hypertension', '(history of) cardio-vascular pathology or abnormal ECG.', 'Presenting signs of acute or active disease at the moment of examination.'],
    'Clinical examples': ['', 'Hormonal replacement therapy, aspirin, ...', 'treated hypothyroidism, stable diabetes, ...', 'Arterial hypertension; β blocking agent, ...', 'Bundle branch block; angina, CABG; ...', 'bronchospasm, swollen joints, influenza, ...'],
}, index=[0, 1, 2, 3, 4, 5])
