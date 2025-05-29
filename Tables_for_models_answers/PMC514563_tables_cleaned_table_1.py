headers: (0,0);(0,1)

import pandas as pd

df = pd.DataFrame({
    'Demographic': ['Gender', 'Male', 'Female', 'Level of Training', 'Clerks', 'First year residents', 'Second year residents', 'Third year residents', 'Fourth year residents', 'Fifth year residents', 'Sixth and above year residents including Fellows', 'University', "Queen's U.", 'U. of Toronto', 'U. of Western Ontario', 'Ottawa U.', 'McMaster U.', 'Mean Age Residents', 'Training Program', 'Medicine', 'Family Medicine', 'Paediatrics', 'Surgery', 'Psychiatry', 'Radiology', 'Intensivists', 'Anaesthesia', 'Laboratory', 'Obstetrics/Gynaecology', 'Emergency'],
    'Study Numbers N (%)': ['N = 1642', '805 (49)', '837 (51)', 'N = 1641', '279 (17.0)', '377 (23.0)', '366 (22.3)', '231 (14.1)', '165 (10.1)', '185 (11.3)', '38 (2.3)', 'N = 1642', '172 (10.5)', '611 (37.3)', '243 (14.8)', '296 (18.0)', '317 (19.3)', '29.9', 'N = 1356*,**', '298 (22.0)', '351 (25.9)', '100 (7.4)', '226 (16.7)', '104 (7.7)', '56 (4.1)', '7 (0.5)', '102 (7.5)', '24 (1.8)', '65 (4.8)', '23 (1.7)'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
