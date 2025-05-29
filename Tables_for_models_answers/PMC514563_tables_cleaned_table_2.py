headers: (0,0);(0,1);(0,2);(0,3);(0,4)

import pandas as pd

df = pd.DataFrame({
    'Rank': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'],
    'Question': ['Effective teachers', 'Opportunity to see patients independently', 'Opportunity to see a large variety of patients', 'Opportunity to see an adequate number of patients', 'Preceptors readily available', 'Opportunity to do procedures', 'Readily available examination room', 'Opportunity to see patients in follow-up visits', 'Opportunity to observe preceptor if desired', 'Opportunity to interact with consultants and/or referring doctors', 'Block rotation', 'Efforts to meet objectives made by preceptor', 'Teaching of medical record keeping skills', 'Computer learning resources available in the clinic', 'Orientation to the practice', 'Teaching of time management skills', 'Teaching of office management skills', 'Clearly defined site objectives for the rotation', 'Library resources available in the clinic', 'Existence of a site-coordinator', 'Longitudinal/horizontal rotation', 'Limited number of preceptors', 'Presence of other trainees in the clinic', 'Close proximity of clinic to campus'],
    'Number saying important to learning (%)': ['1569 (98.4)', '1592 (97.3)', '1511 (94.8)', '1496 (93.9)', '1490 (93.5)', '1357 (85.3)', '1348 (84.8)', '1275 (80.1)', '1239 (77.8)', '1227 (77.1)', '1094 (68.8)', '1059 (66.5)', '956 (60.0)', '947 (59.4)', '937 (59.0)', '904 (56.7)', '872 (54.7)', '843 (52.9)', '778 (48.8)', '762 (48.4)', '603 (38.4)', '443 (27.9)', '432 (27.1)', '366 (23.0)'],
    'Number not answering question': ['4', '6', '4', '5', '4', '8', '9', '6', '6', '7', '7', '5', '4', '3', '11', '3', '4', '5', '4', '22', '29', '13', '4', '8'],
    'Number saying detrimental for learning (%)': ['3 (0.2)', '0', '1 (0.1)', '2 (0.1)', '2 (0.1)', '3 (0.2)', '1 (0.1)', '1 (0.1)', '0', '0', '3 (0.2)', '1 (0.1)', '0', '0', '1 (0.1)', '3 (0.2)', '2 (0.1)', '4 (0.2)', '0', '2 (0.1)', '42 (2.7)', '233 (14.7)', '74 (4.6)', '5 (0.3)'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])
