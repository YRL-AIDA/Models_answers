import pandas as pd

df = pd.DataFrame({
    'NCI CTC Grade': ['Nausea/Vomiting', 'Acute diarrhea', 'Delayed diarrhea', 'Cholinergic syndrome', 'Fever', 'Mucositis', 'Obstipation', 'Asthenia', 'Alopezie'],
    '1': ['9', '3', '4', '2', '3', '5', '8', '2', '9'],
    '2': ['8', '0', '4', '0', '2', '0', '0', '0', '1'],
    '3': ['4', '2', '1', '0', '0', '1', '0', '0', '0'],
    '4': ['0', '1', '1', '0', '0', '0', '0', '0', '0'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8])
