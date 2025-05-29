import pandas as pd

df = pd.DataFrame({
    '': ['α-Mannosidase (= 7)', 'Hexosaminidase (n = 7)', 'Acid lipase (n = 6)', 'Acid phosphatase (n = 6)', 'Glucuronidase (n = 5)', 'Aryl sulphatase (n = 4)'],
    'LSEC': ['0.76 a (0.14)', '30.3 a (7.86)', '6.66 a (2.40)', '11.2 a (3.90)', '3.55 a (0.77)', '0.27 a (0.11)'],
    'KC': ['0.59 b (0,16)', '29.2 a (1.70)', '4.33 ab (2.60)', '8.89 ab (2.72)', '2.35 b (0.53)', '0.20 a (0.05)'],
    'PC': ['0.40 c (0.08)', '4.02 b (2.06)', '2.03 b (0.46)', '4.97 b (1.96)', '0.52 c (0.28)', '0.05 b (0.02)'],
}, index=[0, 1, 2, 3, 4, 5])
