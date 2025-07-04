import pandas as pd

df = pd.DataFrame({
    '': ['Physical functioning', '', 'Social functioning', '', 'Role-physical', '', 'Role-emotional', '', 'Mental health', '', 'Vitality', '', 'Pain index', '', 'General health', ''],
    'N (% completed)': ['654 (96.3%)', '', '654 (96.3%)', '', '638 (94.0%)', '', '630 (92.8%)', '', '653 (96.2%)', '', '649 (95.6%)', '', '655 (96.5%)', '', '651 (95.9%)', ''],
    'CPU care': ['74.1', '', '74.6', '', '54.1', '', '63.9', '', '69.1', '', '52.6', '', '66.4', '', '59.7', ''],
    'Routine care': ['66.2', '', '67.0', '', '46.0', '', '60.2', '', '64.4', '', '47.1', '', '62.0', '', '51.7', ''],
    'Difference Unadjusted Adjusted': ['7.8', '7.6', '7.6', '6.8', '8.2', '7.0', '3.7', '3.9', '4.7', '5.2', '5.5', '5.8', '4.4', '4.3', '8.0', '8.1'],
    '95% CI': ['3.8 to 11.9', '3.6 to 11.5', '3.2 to 12.0', '2.4 to 11.2', '1.3 to 15.0', '0.4 to 13.6', '-3.0 to 10.5', '-2.8 to 10.5', '1.3 to 8.2', '1.9 to 8.6', '1.8 to 9.2', '2.2 to 9.3', '0.2 to 8.5', '0.2 to 8.3', '4.6 to 11.5', '4.6 to 11.5'],
    'P-value': ['<0.001', '<0.001', '0.001', '0.002', '0.02', '0.039', '0.281', '0.256', '0.007', '0.002', '0.003', '0.002', '0.04', '0.041', '<0.001', '<0.001'],
    'ρ': ['0.025', '', '0', '', '0', '', '0', '', '0', '', '0', '', '0', '', '0', ''],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
