headers: (0,0);(0,1);(0,2);(0,3);(0,4);(0,5);(0,6);(0,7);(0,8)

import pandas as pd

df = pd.DataFrame({
    'clone code*': ['PfNPNAl', 'NP04, NP12, NP13', 'R01', 'R02', 'R03', 'R04', 'R05', 'R06', 'R07', 'R08', 'R09', 'R10', 'NP02', 'NP03', 'NP05', 'NP08', 'NP09', 'NP10', 'NP11', 'NP14', 'NP15'],
    'V H family': ['VH3', 'VH3', 'VH1', 'VH3', 'VH5', 'VH3', 'VH3', 'VH1', 'VH5', 'VH5', 'VH3', 'VH1', 'VH3', 'VH5', 'VH3', 'VH4', 'VH4', 'VH4', 'VH3', 'VH1', 'VH5'],
    'V H Segment': ['DP46', 'DP46', '4M28 †‡', 'COS-3 ‡', 'DP73', 'DP46', 'DP58', '4M28 †', 'DP73', 'DP73', 'V3-21 †', 'DP7 ‡', 'DP47', 'DP73', 'V3-48', '4.30 †', 'DP71', 'DP78', 'VH3-8 †', 'DP88', 'DP73'],
    'Differences from germline': ['10', '15', '10', '', '28(+6)* § -', '43', '27 (+3)_', '10', '35', '7', '8', '13', '23', '8', '12', '11', '9', '16', '34', '14', '34', '5', '21 (+9)**', '12', '36', '23', '40', '17', '14', '22', '18', '32', '17', '24', '29', '15', '12', '21', '20', '18', '36', '28'],
    'V H CDR3': ['DRDSSSYFDS', 'DRDSSSYFDS', 'DSESVAQWRY', 'GVNWCSDY', 'LYTSIYYFDS', 'DRVTNFWSGYFDY', 'DSTVKTVTKMRYGLD V', 'DNYGDPGGGFDI', 'RFWFGELYDAFDI', 'LYTSIYYFDS', 'DQGGGWSSEVDS', 'ALYGHDAFDI', 'ERPYDAFDS', 'LYTSIYYFDS', 'EPRGAGTTLYFDY', 'DRGVSSGWTFDC', 'FRGGVAAGYDY', 'DRVRVPYYYIDV', 'DTTVTHYFDY', 'GPGATIHYYYMDV', 'LYTSIYYFDS'],
    'V L family': ['VkI', 'VkI', 'VkIV', 'VkI', 'VkIV', 'VkIII', 'VkIII', 'VkIII', 'VkIV', 'VkIII', 'VkIII', 'VkI', 'VkIII', 'VkIII', 'VkIII', 'VkII', 'VkIII', 'VkIII', 'VkI', 'VkI', 'VkIII'],
    'V L Segment': ['L12a', 'L12a', 'DPK24', 'DPK9', 'DPK24', 'DPK22', 'DPK22', 'DPK22', 'DPK24', 'DPK22', 'Vg', 'DPK4', 'DPK22', 'Vg', 'DPK22', 'DPK16', 'DPK22', 'DPK22', 'DPK9', 'DPK8', 'DPK22'],
    'Differences from germline': ['10', '15', '10', '', '28(+6)* § -', '43', '27 (+3)_', '10', '35', '7', '8', '13', '23', '8', '12', '11', '9', '16', '34', '14', '34', '5', '21 (+9)**', '12', '36', '23', '40', '17', '14', '22', '18', '32', '17', '24', '29', '15', '12', '21', '20', '18', '36', '28'],
    'V L CDR3': ['QQYNSYSGLT', 'QQYNSYSGLT', 'QQSLSPVWT', 'QQSYSTSWT', 'QQYYSTPLT', 'QQYGSSPGFT', 'QQYGSSPFT', 'QQYGNSPRT', 'HQYYSTPQT', 'QQYGRSPWT', 'QQRSNWPLT', 'PKYNSALHT', 'QQYSTSPPMYN', 'KQRSKWPPIT', 'QQYGGSPGYN', 'MQLTAFPWT', 'QHYRESCS', 'QQYGTSPYS', 'QQSFSSPRT', 'QQLDNYPLT', 'QQYGNSPPT'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
