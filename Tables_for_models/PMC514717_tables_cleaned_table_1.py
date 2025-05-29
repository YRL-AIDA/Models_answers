import pandas as pd

df = pd.DataFrame({
    'Enzyme': ['α-Mannosidase', 'Hexosaminidase', 'Glucuronidase', 'Acid phosphatase', 'Aryl sulphatase', 'Acid lipase'],
    'Conc. (mM)': ['2.5', '5.0', '2.5', '1.0', '10.0', '0.3'],
    'Substrate': ['4-methylumbelliferyl-α-D-mannopyranoside', '4-methylumbelliferyl-N-acetyl-β-D-glucosaminide', '4-methylumbelliferyl-β-D-glucuronide', '4-methylumbelliferyl-phosphate', '4-methylumbelliferyl-sulfate', '4-methylumbelliferyl-oleate'],
    'Buffer': ['Phosphate/citrate (0.1 M)', 'Phosphate/citrate (0.1 M)', 'Acetate (0.1 M)', 'Acetate (0.1 M)', 'Acetate (0.5 M)', 'Acetate (0.1 M)*'],
    'pH': ['4.0', '4.5', '4.5', '4.5', '5.5', '4.0'],
    'Incubation time (min)': ['120', '30', '120', '30', '120', '60'],
    'Solubilisate volume (μl)': ['40', '5 10 (PC)', '20 5 (LSEC)', '10', '40', '20'],
}, index=[0, 1, 2, 3, 4, 5])
