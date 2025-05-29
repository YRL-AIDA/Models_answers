import pandas as pd

df = pd.DataFrame({
    'Gene': ['B-cell growth factor (IL-4)', 'CCND1 Cyclin D1 (PRAD1; parathyroid adenomatosis 1)', 'homeobox protein Cdx2 mRNA', 'LIF Leukemia inhibitory factor (cholinergic differentiation factor)', 'tumor susceptiblity protein (TSG101) mRNA', 'carcinoembryonic antigen', 'CCND2 Cyclin D2', 'VIM Vimentin'],
    'PPST Score *': ['13', '13', '12', '10', '-16', '-18', '-18', '-18'],
    'Pattern': ['ABA', 'AB', 'AB', 'AB', 'BA', 'BA', 'BA', 'BA'],
    'p-value under t-test': ['0.301', '0.087', '0.232', '0.181', '0.526', '0.328', '0.076', '0.976'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7])
