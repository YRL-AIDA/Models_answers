headers: (0,0);(0,1);(0,2);(0,3);(0,4);(0,5)

import pandas as pd

df = pd.DataFrame({
    'A': ['', 'vdb', '', '', '', 'B', 'vdb', '', '', '', '', 'C', '', 'Test 2', '', '', '', '', 'D', 'Test 2', '', '', ''],
    '% overlap': ['test', 't-test', 't-test (np)', 'PPST', 'ABA', 'overlap', 'test', 't-test', 't-test (np)', 'PPST', 'ABA', '', 'k', 't-test (p)', 't-test (np)', 'PPST', 'ABA', '', 'v', 't-test (p)', 't-test (np)', 'PPST', 'ABA'],
    'k': ['t-test (p)', '5.307', '', '', '', 'k', 't-test (p)', '35', '', '', '', 'Test 1', 't-test (p)', '1', '', '', '', 'Test 1', 't-test (p)', '1', '', '', ''],
    '': ['t-test (np)', 'PPST', 'ABA', '', '', '', '11.248', '', '', '', '15.24', '', '', '', '3.211', '', '', '', 't-test (np)', 'PPST', 'ABA', '', '', '', '118', '', '', '', '187', '', '', '', '11', '', '', '', 't-test (np)', 'PPST', 'ABA', '78.527', '74.394', '2.579', '1', '83', '4.678', '', '1', '1.28', '', '', '1', '', '', '', 't-test (np)', 'PPST', 'ABA', '46.382', '26.649', '0', '1', '56.975', '5.656', '', '1', '7.268', '', '', '1'],
    '': ['t-test (np)', 'PPST', 'ABA', '', '', '', '11.248', '', '', '', '15.24', '', '', '', '3.211', '', '', '', 't-test (np)', 'PPST', 'ABA', '', '', '', '118', '', '', '', '187', '', '', '', '11', '', '', '', 't-test (np)', 'PPST', 'ABA', '78.527', '74.394', '2.579', '1', '83', '4.678', '', '1', '1.28', '', '', '1', '', '', '', 't-test (np)', 'PPST', 'ABA', '46.382', '26.649', '0', '1', '56.975', '5.656', '', '1', '7.268', '', '', '1'],
    '': ['t-test (np)', 'PPST', 'ABA', '', '', '', '11.248', '', '', '', '15.24', '', '', '', '3.211', '', '', '', 't-test (np)', 'PPST', 'ABA', '', '', '', '118', '', '', '', '187', '', '', '', '11', '', '', '', 't-test (np)', 'PPST', 'ABA', '78.527', '74.394', '2.579', '1', '83', '4.678', '', '1', '1.28', '', '', '1', '', '', '', 't-test (np)', 'PPST', 'ABA', '46.382', '26.649', '0', '1', '56.975', '5.656', '', '1', '7.268', '', '', '1'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
