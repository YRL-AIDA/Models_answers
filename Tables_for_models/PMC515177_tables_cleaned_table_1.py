import pandas as pd

df = pd.DataFrame({
    '4q35 GENE': ['FAT', 'EST a', 'EST b', 'EST c', 'ZFP42/FLJ32157', 'FLJ25801', 'EST d', 'EST e', 'EST f', 'FRG1', 'DUX4'],
    'EST exp.': ['++++', '+', '+', '++', '+', '+', '+++', '+', '+', '++++', '+'],
    'Function/comments': ['Cadherin-related tumor suppressor homologue precursor', '(BE856720) Novel.', '(BM806339) Novel. Contains 5 1/2 copies of 34aa repeat motif', '(AI917275) Novel. No obvious ORF', '(AK056719) Similar to transcriptional repressor protein YY1', '(AK098667) Protein contains SMC (chromosome segregation ATPase) domain and PRY/SPRY domains (unknown function).', '(BU571187) Novel.', '(BC033535) Novel.', '(BC029568) LOC256307 novel predicted gene', 'Facioscapulohumeral muscular dystrophy region gene 1', 'Homeobox protein, multiple copies.'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
