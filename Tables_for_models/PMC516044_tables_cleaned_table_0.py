import pandas as pd

df = pd.DataFrame({
    'Template': ['18S', '', 'KCNJ10', '', 'KCNQ1', '', 'KCNQ4', ''],
    'Primers': ['gag gtt cga aga cga tca ga ( sense )', 'tcg ctc cac caa cta aga ac (antisense)', 'tgg tgt ggt gtg gta tct gg ( sense )', 'tga agc agt ttg cct gtc ac ( antisense )', 'ttt gtt cat ccc cat ctc ag ( sense )', 'gtt gct ggg tag gaa gag ( antisense )', 'ccc gga aac cct tct gtg tc ( sense )', 'aaa gat gag cac cag gaa cc ( antisense )'],
    'Product Length': ['316 bp', '', '411 bp', '', '239 bp', '', '245 bp', ''],
    'Melting Temperature': ['83.2 ± 02°C', '', '83.2 ± 02°C', '', '82.5 ± 02°C', '', '83.2 ± 02°C', ''],
    'Hot Measurement': ['78°C', '', '78°C', '', '79°C', '', '80°C', ''],
    'Fidelity': ['1.89 ± 0.02', '', '1.86 ± 0.02', '', '1.85 ± 0.02', '', '1.87 ± 0.01', ''],
    'n': ['17', '', '15', '', '17', '', '17', ''],
}, index=[0, 1, 2, 3, 4, 5, 6, 7])
