import pandas as pd

df = pd.DataFrame({
    '': ['Ampicillin', 'Amoxicillin/clavulanate', 'Aztreonam', 'Piperacillin', 'Ticarcillin', 'Ticarcillin/clavulanate', 'Cefazolin', 'Cefuroxime', 'Cefotaxime', 'Ceftazidime', 'Ceftriaxone', 'Amikacin', 'Gentamicin', 'Tobramycin', 'Ciprofloxacin', 'İmipenem', 'Tetracycline', 'Cotrimoxazole'],
    'All isolates (n: 90)': ['6', '6', '5', '33', '6', '8', '2', '3', '8', '36', '10', '47', '60', '58', '58', '72', '47', '20'],
    'Gentamicin-resistant (n: 30)': ['2', '3', '1', '4', '2', '5', '1', '-', '1', '5', '1', '2', '-', '24', '21', '25', '17', '10'],
    'Imipenem-resistant (n: 18)': ['-', '-', '1', '1', '-', '-', '-', '1', '1', '6', '1', '6', '11', '17', '11', '-', '10', '5'],
    'Ciprofloxacin-resistant (n: 32)': ['-', '-', '-', '9', '1', '1', '-', '-', '-', '7', '-', '13', '25', '28', '-', '26', '6', '6'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
