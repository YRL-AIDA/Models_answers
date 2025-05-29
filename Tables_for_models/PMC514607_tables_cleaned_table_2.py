import pandas as pd

df = pd.DataFrame({
    'Indications': ['Clinical suspicion', 'Contacts of patients', 'Blood donors', 'Hemophilia and other blood disorders', 'Before surgery', 'Prisoners', 'Intravenous drug users', 'Patients on hemodialysis', 'Pre-employment', 'Patients with tuberculosis', 'Self-request', 'Pregnancy', 'Total'],
    'Number': ['438', '190', '146', '113', '96', '84', '56', '51', '46', '36', '19', '10', '1285'],
    '%': ['34', '15', '11', '9', '7', '7', '4', '4', '4', '3', '1', '1', '100'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
