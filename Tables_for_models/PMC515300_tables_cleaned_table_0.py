import pandas as pd

df = pd.DataFrame({
    'Antibiotics': ['Ampicillin', 'Amoxicillin/clav.', 'Aztreonam', 'Piperacillin', 'Cefazolin', 'Cefuroxime', 'Cefotaxime', 'Ceftazidime', 'Ceftriaxone', 'Amikacin', 'Gentamicin', 'Tobramycin', 'Ciprofloxacin', 'İmipenem', 'Tetracycline', 'Cotrimoxazole'],
    'Klebsiella spp (n: 28)': ['-', '7.1', '42.9', '32.1', '64.3', '46.4', '67.9', '71.4', '71.4', '92.9', '82.1', '10.7', '92.9', '100.0', '-', '64.3'],
    'E.coli (n: 18)': ['33.3', '33.3', '44.4', '27.8', '66.7', '66.7', '72.2', '72.2', '88.9', '100.0', '100.0', '16.6', '88.9', '100.0', '22.2', '55.6'],
    'Proteus spp. (n: 10)': ['-', '-', '50.0', '50.0', '50.0', '40.0', '90.0', '70.0', '90.0', '100.0', '80.0', '-', '90.0', '80.0', '20.0', '70.0'],
    'Enterobacter spp (n: 10)': ['-', '-', '60.0', '30.0', '10.0', '40.0', '100.0', '90.0', '90.0', '100.0', '90.0', '41.7', '70.0', '100.0', '20.0', '100.0'],
    'A. baumanii (n: 7)': ['-', '-', '-', '-', '14.3', '-', '-', '14.3', '-', '28.6', '85.7', '14.3', '42.9', '100.0', '-', '14.3'],
    'Serratia spp. (n: 6)': ['-', '-', '33.3', '33.3', '-', '-', '66.7', '50.0', '50.0', '100.0', '100.0', '33.3', '100.0', '100.0', '16.7', '100.0'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
