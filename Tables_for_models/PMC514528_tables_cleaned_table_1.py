import pandas as pd

df = pd.DataFrame({
    'Gene name': ['Catenin (cadherin assoc. protein) beta 1', 'Interleukin 8*', 'Granulysin*', 'Caspase 2*', 'Interleukin 24', 'Heat shock protein (HSP 110 family)*', 'TP53 (Li Fraumeni)*', 'Toll-like receptor 2 (TLR-2)', 'Heat shock protein 70*', 'Granzyme A', 'Interleukin 1β', 'Survivin', 'Calreticulin', 'Human Natural killer Cell enhancing factor', 'CD68 antigen', 'ICAM 1 (CD54)', 'Interleukin 18 (interferon-gamma inducing factor)*', 'Interleukin 7', 'Interleukin 15*', 'Gene name', 'Insulin-like growth factor 2 (somatomedin A)', 'TGFβ RII', 'hMLH 1*'],
    'P value': ['6.5 × 10 -12', '1.7 × 10 -4', '1.3 × 10 -7', '6.0 × 10 -8', '0.004', '2.4 × 10 -5', '2.5 × 10 -4', '1.9 × 10 -4', '3.5 × 10 -6', '0.001', '0.004', '0.001', '2.9 × 10 -5', '0.001', '4.8 × 10 -4', '0.003', '0.003', '4.6 × 10 -4', '0.002', 'P value', '1.9 × 10 -5', '9.3 × 10 -5', '6.7 × 10 -5'],
    'Fold change': ['2.9', '2.8', '2.8', '2.4', '2.3', '2.2', '2.2', '1.9', '1.8', '1.7', '1.7', '1.6', '1.6', '1.6', '1.6', '1.6', '1.5', '1.5', '1.5', 'Fold change', '4.3', '3.0', '2.4'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
