import pandas as pd

df = pd.DataFrame({
    '': ['Positive cases', 'Negative cases', 'Statistics (comparison)', 'Intensity (avg+/-std)', 'Percentage cells (avg+/- std)', 'Nuclear cases', 'Cytoplasmic cases', 'Statistics (comparison)', 'Positive cases', 'Negative cases', 'Statistics (comparison)', 'Intensity (avg+/-std)', 'Percentage cells (avg+/- std)', 'Nuclear cases', 'Cytoplasmic cases', 'Statistics (comparison)'],
    'Normal Prostate': ['105', '5', '', '2.47 +/- 0.70', '8.3 +/- 13.5', '92', '22', '', '92', '10', '', '2.73 +/- 0.51', '20.0 +/- 25.5', '92', '2', ''],
    'Nodular Hyperplasia': ['62', '1', 'p = 0.0036 (cancer)', '2.49 +/- 0.65', '7.5 +/- 12.5', '59', '6', 'p < 0.00001 (cancer)', '58', '3', 'p < 0.00001 (cancer)', '2.78 +/- 0.50', '23.2 +/- 25.7', '58', '0', 'N.S. (cancer)'],
    'HGPIN': ['49', '9', 'N.S. (cancer)', '2.57 +/- 0.82', '8.8 +/- 15.2', '40', '18', 'p = 0.065 (cancer)', '35', '31', 'N.S. (cancer)', '2.83 +/- 0.38', '8.4 +/- 12.5', '35', '6', 'N.S. (cancer)'],
    'Prostate Cancer': ['202', '36', 'p = 0.0044 (normal)', '2.74 +/- 0.56', '4.4 +/- 6.6', '94', '152', 'p < 0.00001 (normal)', '112', '125', 'p < 0.00001 (normal)', '2.76 +/- 0.49', '8.6 +/- 12.6', '107', '9', 'N.S. (normal)'],
    'Metastatic Cancer': ['25', '8', 'N.S. (cancer)', '2.79 +/- 0.49', '8.5 +/- 12.6', '8', '11', 'N.S. (cancer)', '16', '19', 'N.S. (cancer)', '3 +/- 0', '4.2 +/- 4.6', '16', '0', 'N.S. (cancer)'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
