import pandas as pd

df = pd.DataFrame({
    'Name a': ['ACT11', 'ACT2', 'CYP', 'TUA', 'TUB', 'UBQ', 'UBQ-L', 'EIF4B-L', 'EF1β', '18S'],
    'GenBank accession number b': ['CA824001', 'BU879695', 'BU875027', 'CA822230 CA825391', 'CA824237', 'BU879229', 'BU871588', 'CA825614', 'BI125345', 'AF206999'],
    'Arabidopsis homolog locus c': ['AT3G12110', 'AT5G09810', 'AT2G21130', 'AT5G19780', 'AT4G20890', 'AT4G05050', 'AT2G35635', 'AT4G38710', 'AT2G18110', '18RRNA'],
    'Arabidopsis locus description': ['Actin 11', 'Actin 2/7', 'cyclophilin (CYP2)', 'tubulin alpha-3/alpha-5 chain', 'tubulin beta-9 chain', 'polyubiquitin (UBQ11)', 'ubiquitin-like (UBQ7)', 'similarity to eukaryotic translation initiation factor 4B', 'elongation factor 1-beta, putative', '18S ribosomal RNA'],
    'BLASTX score/ E value': ['363/ e-101', '320/ 5e-088', '284/ 6e-077', '439/ e-130', '154/ 4e-038', '416/ e-117', '291/ 4e-079', '80/ 1e-015', '122/ 1e-028', '2949/ 0.0'],
    'Primer sequences (forward/reverse)': ['CACACTGGAGTGATGGTTGG / ATTGGCCTTGGGGTTAAGAG', 'CCCATTGAGCACGGTATTGT / TACGACCACTGGCATACAGG', 'GGCTAATTTTGCCGATGAGA / ACGTCCATCCCTTCAACAAC', 'AGGTTCTGGTTTGGGGTCTT / TTGTCCAAAAGCACAGCAAC', 'GCACCAACTTGTTGAGAATGC / TTTCAACTGACCAGGGAACC', 'GTTGATTTTTGCTGGGAAGC / GATCTTGGCCTTCACGTTGT', 'TGAGGCTTAGGGGAGGAACT / TGTAGTCGCGAGCTGTCTTG', 'AAAAAGGGGATTTGGGATTG / AACTTCGTCCTCGGTAGCAA', 'AAGAGGACAAGAAGGCAGCA / CTAACCGCCTTCTCCAACAC', 'AATTGTTGGTCTTCAACGAGGAA/ AAAGGGCAGGGACGTAGTCAA'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
