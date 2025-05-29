import pandas as pd

df = pd.DataFrame({
    'Journal Title': ['New England Journal of Medicine', 'JAMA', 'Archives of General Psychiatry', 'Circulation', 'Lancet', 'Annals of Internal Medicine', 'Annals of Neurology', 'Journal of the American College of Cardiology', 'Psychological Bulletin', 'Arthritis and Rheumatism', 'American Journal of Psychiatry', 'Archives of Internal Medicine', 'American Journal of Medicine', 'American Journal of Respiratory and Critical Care Medicine', 'Gut', 'BMJ', 'Hypertension', 'Diabetes Care', 'Journal of Infectious Diseases'],
    'SCI Impact Factor': ['29.521', '15.402', '11.778', '10.893', '10.232', '9.833', '8.480', '7.082', '6.913', '6.841', '6.577', '6.055', '5.960', '5.443', '5.386', '5.331', '5.311', '4.992', '4.988'],
    'Qualitative Studies': ['0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '12', '0', '1', '0'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
