import pandas as pd

df = pd.DataFrame({
    'GENE NAME': ['SIC1', 'CLN1', 'CLN2', 'CLN3', 'SWI4', 'SWI6', 'CLB5', 'CLB6', 'CDC6', 'CDC20', 'CDC28', 'MBP1'],
    'ORF': ['YLR079W', 'YMR199W', 'YPL256C', 'YAL040C', 'YER111C', 'YLR182W', 'YPR120C', 'YGR109C', 'YJL194W', 'YGL116W', 'YBR160W', 'YDL056W'],
    'DESCRIPTION': ['inhibitor of the Cdc28-Clb protein kinase complex', 'G1/S-specific cyclin', 'G1/S-specific cyclin', 'G1/S-specific cyclin', 'transcription factor, subunit of the SBF factor', 'transcription factor, subunit of SBF and MBF (check this)', 'B-type cyclin', 'B-type cyclin', 'initiates DNA replication, active late G1/S', 'cell division control protein', 'cyclin-dependent protein kinase', 'transcription factor, subunit of MBF'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
