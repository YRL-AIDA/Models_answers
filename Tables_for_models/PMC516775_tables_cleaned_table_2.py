import pandas as pd

df = pd.DataFrame({
    'Clone name': ['dd3', 'dd4', 'dd6', 'dd11'],
    'Clone length (bp)': ['774', '1533', '2192', '1588'],
    'Accession N°': ['AJ634908', 'AJ635428', 'AJ629867', 'AJ629866'],
    'Matching sequence from data base': ['Ras-related GTP-binding protein', 'Translation releasing factor 2', 'β-1,4- N -acetylglucosaminyltranferase', 'Pathogenesis-related protein'],
    'Origin of matching sequence and accession number': ['A. thaliana NP 177505', 'A. thaliana NP 851097', 'A. thaliana NP 172759', 'A. thaliana NP 565189'],
    'Amino acid sequence % identity (*)': ['65 % (1e -73 )', '70 % (7e -170 )', '77 % (0.0)', '51 % (1e -51 )'],
}, index=[0, 1, 2, 3])
