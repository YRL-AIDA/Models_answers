headers: (0,0);(0,1);(0,2);(1,2);(1,3)

import pandas as pd

df = pd.DataFrame({
    'Gene': ['Hs.155376_at', 'Hs.36977_at', 'Hs.203820_at', 'Hs.21295_at', 'Hs.247921_at', 'Hs.87246_at', 'Hs.256047_at', 'Hs.14587_at', 'Hs.117848_at', 'Hs.168073_at', 'Hs.24545_at', 'Hs.6318_at', 'Hs.155833_at', 'Hs.109857_at', 'Hs.248677_at', 'Hs.4205_at', 'Hs.106876_at', 'Hs.172914_at', 'Hs.23898 at'],
    'Description': ['haemoglobin, beta', 'haemoglobin, delta EST, similar to tctp human translationally controlled tumor protein H. sapiens', '', 'EST, Weakly similar to KIAA0902 protein H. sapiens', 'haemoglobin, theta 1', 'Bcl-2 binding component 3', 'ESTs, similar to B24264 proline-rich protein MP3 - M. musculus', 'ESTs, similar to AF1 51 859_1 CGI-101 protein H. sapiens', 'haemoglobin, epsilon 1', 'DKFZP727M231 protein', 'hypothetical protein FLJ11137', 'peroxisomal short-chain alcohol dehydrogenase', 'ESTs, similar to spliceosomal protein SAP 155 H. sapiens Homo sapiens mRNA; cDNA DKFZp434H0820 (from clone DKFZp434H0820); partial cds', '', 'ESTs, similar to A48018 mucin 7 precursor, salivary – H. sapiens', 'hypothetical protein FLJ20124 ATPase, H+ transporting, lysosomal (vacuolar proton pump), member D', '', 'retinol dehydrogenase 5 (11-cisand 9-cis)', 'paraneoplastic antigen'],
    'in vivo': ['757266', '395849', '241506', '190454', '188961', '187575', '160290', '155768', '150921', '147492', '146324', '145846', '140563', '138856', '136390', '132244', '127582', '125310', '124648'],
    'in vitro 3D7': ['101307', '12265', '6932', '9321', '4528', '5688', '5681', '6389', '5903', '6615', '6292', '5136', '5508', '7397', '5253', '4050', '3930', '4560', '5631'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
