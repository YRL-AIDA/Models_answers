import pandas as pd

df = pd.DataFrame({
    'No': ['1', '', '2', '', '3', '', '4', '', '5', '', '1', '', '2', '', '3', '', '4', '', '5', '', '1', '2', '3', '4', '5'],
    ' Concentration of hypochloric acid ': ['before', '12.5 ppm after', 'before', '12.5 ppm after', 'before', '12.5 ppm after', 'before', '12.5 ppm after', 'before', '12.5 ppm after', 'before', '6.25 ppm after', 'before', '6.25 ppm after', 'before', '6.25 ppm after', 'before', '6.25 ppm after', 'before', '6.25 ppm after', 'Control group', '', '', '', ''],
    'Transport fluid Colony count': ['12', 'No reproduction', '23', 'No reproduction', '30', 'No reproduction', '25', 'No reproduction', '18', 'No reproduction', 'No reproduction', 'No reproduction', '27', 'No reproduction', '20', 'No reproduction', 'No reproduction', 'No reproduction', '15', 'No reproduction', 'Not studied', 'Not studied', 'Not studied', 'Not studied', 'Not studied'],
    'Mouth Colony count': ['16', 'No reproduction', '14', 'No reproduction', '34', 'No reproduction', '16', 'No reproduction', 'No reproduction', 'No reproduction', '20', 'No reproduction', '7', 'No reproduction', 'No reproduction', 'No reproduction', '8', 'No reproduction', '12', 'No reproduction', 'Not studied', 'Not studied', 'Not studied', 'Not studied', 'Not studied'],
    'Gut Colony count': ['Not studied', '25', 'Not studied', '18', 'Not studied', '50', 'Not studied', '44', 'Not studied', '30', 'Not studied', '100', 'Not studied', '120', 'Not studied', '72', 'Not studied', '95', 'Not studied', '75', '100', '150', '120', '105', '140'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])
