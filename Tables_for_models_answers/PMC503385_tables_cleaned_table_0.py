headers: (0,0);(0,1);(0,2);(0,3);(0,4)

import pandas as pd

df = pd.DataFrame({
    'Strain*': ['R538', 'R539', 'R540', 'R541', 'R542', 'R543', 'R652, R3460*, R3539*, R3540*, R3541*, R3542*', 'Strain', 'C378, C483, C1591, C1607, R1624, R1625, R1627, R1632, R2754, R3254, R3256, R3258, R3259, R3262, R3264, R3265, R3266, R3267, R3268, R3269, R3271, R3273, R3274, R3276. R3277, R3282, R3283, R3285', 'R3257, R3270', 'R2752, R3001, R3027, R3157, R3543*', 'R296, R2751, R2846, R3151', 'C432, R228, R2777, R3168, R3252, R3278, R3279, R3280, R3330, R3331', 'R2866, R3122, R3164, R3169'],
    'Description': ['ATCC #9795', 'ATCC #9006', 'ATCC #9007', 'ATCC #9008', 'ATCC #8142', 'ATCC #9833', 'Rd', 'Anatomical site  ‡ ', 'Nasopharynx', '', 'Sputum/Tracheal Aspirate/Ear', '', 'Blood/CSF', ''],
    'Type': ['b', 'a', 'c', 'd', 'e', 'f', 'NTHi', 'Type', 'NTHi', '', 'NTHi', '', 'NTHi', ''],
    ' vapD    Hi   allele  † ': ['WT', 'WT', 'WT', 'WT', 'WT', 'WT', 'WT', ' vapD    Hi   allele', 'WT', 'TV', 'WT', 'TV', 'WT', 'TV'],
    'Prevalence': ['100%', '', '', '', '', '', '', 'Prevalence', '93% (28/30)', '7%', '50% (4/8)', '50%', '71% (10/14)', '29%'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
