import pandas as pd

df = pd.DataFrame({
    'Responder status, n (%)': ['Full', 'Partial', 'None', 'Full response (n = 25)', 'Partial response (n = 17)', 'Median time to full response, days', 'Median time to partial response, days', 'Full response', 'Partial response', 'Full response', 'Partial response', 'Modal daily dosage for full response, mg/day', '% of patients in the 12.5–50-mg/day range', 'Modal dosage at time of partial response, mg/day', '% of patients in the 12.5–50-mg/day range', 'Full cessation of nightmares', 'Full cessation of intrusions', 'Partial improvement', 'No improvement'],
    '': ['26/33 (79%)', '3/33 (9%)', '4/33 (12%)', '15 ± 18 (1–83)', '11 ± 13 (2–46)', '9', '5', '60 ± 47', '32 ± 15', '50', '25', '25', '65', '25', '100', '17/18 (94%)', '26/33 (79%)', '3/33 (9%)', '4/33 (12%)'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
