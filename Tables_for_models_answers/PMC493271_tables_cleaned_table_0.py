headers: (0,0);(0,1);(0,4);(0,5);(1,1);(1,2);(1,3)

import pandas as pd

df = pd.DataFrame({
    'Characteristics': ['Number of subjects', 'Mean and SD of mahchine-measured nicotine yield (mg/cigarette)', 'Mean and SD of age', 'Mean and SD of number of cigarettes per day', 'Mean and SD of FTND', 'FTND score 0–3', 'FTND score 4–6', 'FTND score 7–10', 'Number of smokers having attempted to quit', 'Precontemplation-1', 'Precontemplation-2', 'Contemplation', 'Preparation', 'Mean and SD of urinary cotinine concentration (mean-SD, mean+SD*)'],
    '0.1': ['87', '0.1', '53.6 ± 10.4', '23.4 ± 12.2', '5.1 ± 2.5', '19 (21.8%)', '40 (46.0%)', '28 (32.2%)', '50 (61.0%)', '16 (18.6%)', '48 (55.8%)', '20 (23.3%)', '2 (2.3%)', '535 (1782,160)'],
    '0.2–0.8': ['223', '0.5 ± 0.2', '50.6 ± 9.34', '24.5 ± 10.7', '5.4 ± 2.3', '47 (21.1%)', '100 (44.8%)', '76 (34.1%)', '132 (59.5%)', '47 (21.3%)', '131 (59.3%)', '33 (14.9%)', '10 (4.5%)', '770 (1981,299)'],
    '0.9–2.4': ['148', '1.1 ± 0.4', '50.8 ± 10.4', '24.4 ± 9.5', '5.6 ± 2.0', '21 (14.2%)', '78 (52.7%)', '49 (33.1%)', '84 (56.8%)', '58 (39.7%)', '62 (42.5%)', '23 (15.6%)', '3 (2.1%)', '1010 (2071,492)'],
    'Total': ['458', '0.6 ± 0.4', '51.2 ± 9.9', '24.4 ± 10.6', '5.4 ± 2.2', '87 (19.0%)', '218 (47.6%)', '153 (33.4%)', '269 (58.9%)', '121 (26.7%)', '241 (53.2%)', '76 (16.8%)', '15 (3.3%)', '784 (484, 1264)'],
    'p': ['', '', '0.07', '0.93', '0.21', '', '0.41', '', '0.73', '0.001', '', '', '', '<0.001'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
