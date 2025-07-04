import pandas as pd

df = pd.DataFrame({
    '': ['1 ( not at all satisfied )', '2', '3', '4', '5', '6', '7 ( completely satisfied )', 'certainly not', 'probably not', 'yes probably', 'yes certainly', 'certainly not', 'probably not', 'yes probably', 'yes certainly', 'To consult again', 'Do not agree', 'agree', 'Fully agree', 'negative comment', 'mixed comment', 'no comment', 'positive comment'],
    'n': ['13', '', '12', '', '18', '-', '39', '', '125', '', '285', '', '496', '', '13', '-', '30', '', '272', '', '665', '', '10', '-', '20', '', '213', '', '756', '', '', '9', '-', '46', '', '18', '', '1', '303', '85', '110', '8', '442', '91', '152', '42'],
    'Score (sd) (1)': ['58.0 (21.6)', '68.7 (17.7)', '56.0 (13.5)', '59.4 (14.0)', '72.1 (11.5)', '80.3 (10.0)', '90.6 (7.6)', '52.7 (18.2)', '57.3 (16.7)', '75.4 (13.1)', '87.6 (9.5)', '58.7 (24.2)', '57.3 (17.9)', '72.5 (14.5)', '86.6 (10.3)', '', 'na', '', '', '76.1 (14.7)', '78.4 (13.5)', '85.4 (12.1)', '91.2 (8.2)'],
    'P': ['', '', '', '', '<0.001 (4)', '-', '', '', '', '', '', '', '', '', '<0.001 (4)', '-', '', '', '', '', '', '', '<0.001 (4)', '-', '', '', '', '', '', '', '', '', '-', '<0.001', '', '', '', '', '', '', '<0.001', '<0.001', '', '', '', ''],
    'n': ['13', '', '12', '', '18', '-', '39', '', '125', '', '285', '', '496', '', '13', '-', '30', '', '272', '', '665', '', '10', '-', '20', '', '213', '', '756', '', '', '9', '-', '46', '', '18', '', '1', '303', '85', '110', '8', '442', '91', '152', '42'],
    'Score (sd) (2)': ['', '', 'na', '', '', '', '', 'na', '', '', '', 'na', '', '', '', '', '57.8 (14.4)', '64.2 (12.4)', '84.3 (11.7', '72.1 (14.9)', '81.0 (12.4)', '82.0 (15.8)', '85.5 (11.1)'],
    'P': ['', '', '', '', '<0.001 (4)', '-', '', '', '', '', '', '', '', '', '<0.001 (4)', '-', '', '', '', '', '', '', '<0.001 (4)', '-', '', '', '', '', '', '', '', '', '-', '<0.001', '', '', '', '', '', '', '<0.001', '<0.001', '', '', '', ''],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
