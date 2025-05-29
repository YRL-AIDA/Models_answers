import pandas as pd

df = pd.DataFrame({
    'Virtual Signature Class': ['0*', '1', '2', '3', '4', '5', '6', '11', '12', '13', '14', '15', '16', '22', '23', '24', '25', '26', '1000***'],
    'MRNA Orientation': ['Either – Repeat Warning', 'Forward Strand', '', '', '', '', '', 'Reverse Strand', '', '', '', '', '', 'Unknown', '', '', '', '', 'Unknown – Derived from Genomic Sequence'],
    'Poly-Adenelation Features **': ['Not applicable', 'Poly-A Signal, Poly-A Tail', 'Poly-A Signal', 'Poly-A Tail', 'None', 'None', 'Internal Poly-A', 'Poly-A Signal, Poly-A Tail', 'Poly-A Signal', 'Poly-A Tail', 'None', 'None', 'Internal Poly-A', 'Poly-A Signal', 'Poly-A Tail', 'None', 'None', 'Internal Poly-A', 'Not applicable'],
    'Position': ['Not applicable', "3' most", "3' most", "3' most", "3' most", "Not 3' most", "Not 3' most", "5' most", "5' most", "5' most", "5' most", "Not 5' most", "Not 5' most", 'Last before signal', 'Last before tail', 'Last in sequence', 'Not last', "Not 3' most", 'Not applicable'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
