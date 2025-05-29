headers: (0,0);(0,1);(0,2)

import pandas as pd

df = pd.DataFrame({
    'Rank': ['1', '2', '3', '4', '', '', '5', '', '6', '', '', '', '', '', '', '7', '', '8', '', 'Rank', '1', '2', '3', '4', '', '', '5', '6', '7', '8', '9', 'Rank', '1', '2', '', '', '3', '', '', '', '4', '5'],
    'Topic': ['Sector Analysis', 'Disease burden', 'Management & organization', 'Accessibility', 'Programme evaluation', 'Research to evidence', 'Financing', 'Human resources', 'Community participation', 'Costing & cost effectiveness', 'Decentralisation/local health systems', 'Information, Education and Communication', 'Insurance', 'Pharmaceutical policy & management', 'Quality', 'Equity', 'Policy process', 'Economic policy and health', 'Information systems', 'Beneficiaries/Issue', 'Community', 'Equity/poverty', 'Hospital', '1st level', 'Gender/women', 'Rural areas', 'Children/adolescents', 'Public private mix', 'Urban areas', 'Elderly', 'Indigenous peoples/traditional medicine', 'Health Problem', 'Reproductive health', 'HIV-AIDS', 'Nutrition', 'TB', 'Chronic', 'Environmental health', 'Malaria', 'Mental health', 'Other infectious', 'Other'],
    '%': ['11', '9', '8', '7', '7', '7', '6', '6', '4', '4', '4', '4', '4', '4', '4', '3', '3', '2', '2', '%', '15', '14', '12', '11', '11', '11', '10', '6', '5', '4', '3', '%', '30', '11', '11', '11', '7', '7', '7', '7', '6', '3'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41])
