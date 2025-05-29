import pandas as pd

df = pd.DataFrame({
    'Tissue': ['Liver 1', 'Liver 2', 'Kidney 1', 'Kidney 2', 'Breast', 'Lung 1', 'Lung 2'],
    'Normal': ['0.107', '2.357', '0.306', '0.272', '0.051', '0.018', '0.026'],
    'Tumor': ['0', '0', '0.051', '0.299', '0.014', '0.002', '0.779'],
    'Tumor/normal': ['0', '0', '0.17', '1.10', '0.27', '0.11', '29.97'],
}, index=[0, 1, 2, 3, 4, 5, 6])
