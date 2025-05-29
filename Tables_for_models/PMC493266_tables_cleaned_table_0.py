import pandas as pd

df = pd.DataFrame({
    'Functional class': ['Amino acid metabolism', 'Biosynthesis of cofactors, prosthetic groups, carriers', 'Cell envelope', 'Cellular process', 'Central intermediary metabolism', 'Energy metabolism', 'Fatty acid/Phospholipid metabolism', 'Hypothetical', 'Nucleotide metabolism', 'Other categories', 'Regulatory functions', 'Replication', 'Transcription', 'Translation', 'Transport/binding protein', 'Total'],
    '"GATC genes"': ['2', '2', '2', '1', '4', '16', '8', '11', '11', '3', '1', '4', '1', '0', '10', '76'],
    "all of E. coli 's genes": ['134', '127', '194', '102', '149', '363', '64', '1847', '120', '236', '104', '89', '47', '150', '369', '4095'],
    '"EcoCyc genes"': ['0', '2', '5', '18', '9', '6', '1', '12', '2', '30', '12', '14', '5', '2', '28', '146'],
    '"Mitomycin C genes"': ['5', '1', '10', '14', '15', '29', '4', '62', '14', '15', '5', '19', '7', '61', '42', '303'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
