import pandas as pd

df = pd.DataFrame({
    '': ['Age (quantitative variable)', 'Matrimonial status (Married or living with partner v. single v. divorced, separated, or widowed)', 'Working status (employed v. student v. unemployed v. Retired v. prolonged sick leave v. other)', 'Level of education (university yes v. no)', 'Overall satisfaction with life (quantitative variable)', 'Outpatient department (n = 10)', '# of consultations in the department (first v. 2 to 3 v. 4 to 5 v. more then 5)', 'At least one hospitalization in the ward', 'Duration of the health problem justifying the consultation (less than 6 month v. 6 month and more)', "Severe medical problem ('yes definitely' v. 'yes rather' v. 'neither yes nor no', v. 'not really', v. 'definitely not' v. 'do not know')", 'Comorbidity (yes v. no)', 'Perceived health status, compared to persons of same age (better v. similar v. worse)'],
    'DF': ['1', '2', '5', '1', '1', '9', '3', '1', '1', '5', '1', '2'],
    'F-value': ['7.75', '0.93', '0.79', '1.72', '51.1', '4.3', '2.92', '0.73', 'FGF', '1.19', '1.97', '0.49'],
    'P-value': ['0.006', '0.42', '0.56', '0.19', '0.001', '0.001', '0.03', '0.39', '0.22', '0.31', '0.16', '0.61'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
