headers: (0,0);(0,1);(0,2);(0,3);(0,4)

import pandas as pd

df = pd.DataFrame({
    'SIGNATURE': ['GATCTCCAGTAGACTTA', 'GATCTGTTAACAAAGGA', 'GATCTAGAAGTTGCAAC', 'GATCTTTTTTTTTGCCC', 'GATCCCCATCCAAAAGA', 'GATCCACCTAGGACCTC', 'GATCCGCCTCCTTGGCC', 'GATCCTAGCCAAGCCCC', 'GATCTGGCCCGCCACCA', 'GATCGTTGTGGTGGACT', 'GATCCACCACATGGCGA', 'GATCCAACAATTCTACT', 'GATCTTCTAAACCCATC'],
    'HuES,TPM': ['1646', '967', '489', '455', '366', '244', '240', '169', '150', '146', '92', '78', '75'],
    'Chr': ['4', '16', '1', '3', '7', 'X', '4', '3', '16', '3', '11', 'U', '12'],
    'GB:description': ['CD250365:Homo sapiens transcribed sequence **', 'BC008934:claudin 6', 'NM_019079:hypothetical protein FLJ10884', 'NM_018189:hypothetical protein FLJ10713', 'AI636928:Homo sapiens transcribed sequences', 'CD174249:Homo sapiens transcribed sequence', 'AK092578:Sapiens cDNA FLJ35259 fis', 'BF223023:Homo sapiens transcribed sequences', 'NM_032805:hypothetical protein FLJ14549 (ZNF206)', 'XM_067369:similar to Heterochronic gene LIN-41', 'CD176172:Homo sapiens transcribed sequence', 'CD173198:Homo sapiens transcribed sequences', 'BU608353:Homo sapiens transcribed sequence'],
    'Other 36, TPM*': ['NS-10', 'ND', 'ND', 'TH-47, HY-3, PG-3', 'MCF7-2', 'ND', 'ND', 'ND', 'ND', 'ND', 'ND', 'TE-33', 'ND'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
