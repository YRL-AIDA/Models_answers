headers: (0,0);(0,1);(0,2);(0,3);(0,4);(0,5)

import pandas as pd

df = pd.DataFrame({
    'Organism': ['Bemisia tabaci', 'Tetraleurodes acaciae', 'Neomaskellia andropogonis', 'Aleurochiton aceris', 'Trialeurodes vaporariorum', 'Aleurodicus dugesii', 'Pachypsylla venusta', 'Schizaphis graminum', 'Bemisia argentifolii', 'Bemisia sp.', '', 'Aleuroplatus sp.', 'Tetraleurodes mori', 'Vasdavidius concursus', 'Siphonius phillyreae', 'Bactericera cockerelli', 'Calophya schini', 'Glycaspis brimblecombei', 'Diuraphis noxia', 'Melaphis rhois', 'Schlechtendalia chinensis', 'Daktulosphaira vitifoliae'],
    'Type': ['whitefly-A', 'whitefly-B', 'whitefly-C', 'whitefly-D', 'whitefly-Y', 'whitefly-Y', 'psyllid', 'aphid', 'whitefly-A', 'whitefly-A', '', 'whitefly-B', 'whitefly-B', 'whitefly-C', 'whitefly-D', 'psyllid', 'psyllid', 'psyllid', 'aphid', 'aphid', 'aphid', 'phylloxera'],
    'Mitochondrial sequence': ['complete', 'complete', 'complete', 'complete', 'complete', 'complete', 'complete', 'complete', 'cytB-COIII', '12S-COIII', 'cytB-12S', 'cytB-COIII', 'cytB-COIII', 'cytB-COIII', 'cytB-12S', 'cytB-12S', 'cytB-12S', 'cytB-12S', 'cytB-12S', 'cytB-12S', 'cytB-12S', 'cytB-12S'],
    'Size (bp)': ['15,322', '15,080', '14,496', '15,388', '18,414', '15,723', '14,711', '15,721', '4, 796', '985', '', '4, 540', '4,416', '3,374', '4,561', '3,077', '3,044', '3,081', '3,180', '3,184', '3,188', '3,215'],
    'G+C content': ['25.9', '28.0', '18.7', '22.1', '27.7', '13.8', '26.3', '16.1', '23.2', '19.4', '', '27.4', '25.3', '20.0', '22.3', '28.0', '26.3', '26.8', '15.8', '17.0', '16.1', '22.6'],
    'GenBank accession number': ['AY521259', 'AY521626', 'AY572539', 'AY572538', 'AY521265', 'AY521251', 'AY278317', 'AY531391', 'AY521257', 'AY572845', 'AY521257 a', 'AY521256', 'AY521263', 'AY648941', 'AY521268', 'AY601890', 'AY601891', 'AY601889', 'AY601892', 'AY601894', 'AY601893', 'AY601895'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
