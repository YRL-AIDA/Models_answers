headers: (0,0);(0,1);(0,2)

import pandas as pd

df = pd.DataFrame({
    'GenBank': ['L09119', 'S77867', 'AF109405', 'U08290', 'M15880', 'S56508', 'AF041083', 'X86789'],
    'Name': ['C kinase substrate calmodulin-binding protein (neurogranin) (shown in Fig. 3)', 'G coupled protein receptor UHR-1 (G protein coupled receptor 10)', 'GABA-B receptor 2 (G protein-coupled receptor 51)', 'Neuronatin alpha (neuronatin)', 'Neuropeptide Y (shown in Fig. 3)', 'Fatty acid coenzyme A ligase, long chain 6', 'RoBo-1 (Slc11a1) (shown in Fig. 3)', 'Sensory neuron synuclein (gamma-synuclein)'],
    'Reference': ['[89]', '[90]', '[91]', '[92]', '[93,94]', '[95]', '[55,96,97]', '[98,99]'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7])
