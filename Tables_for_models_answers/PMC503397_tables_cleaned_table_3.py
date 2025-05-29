headers: (0,0);(0,1);(0,2);(0,3);(0,4);(0,5);(0,6)

import pandas as pd

df = pd.DataFrame({
    'Category': ['Phenomenology', 'Grounded Theory', 'Ethnography', 'Case Studies', 'Narratives', 'Participatory', 'Critical Incident Technique', 'Discourse Analysis', 'Semi-structured Interviews', 'Observation', 'Focus Groups', 'Questionnaires', 'Documents', 'Unstructured Interviews', 'Structured Interviews'],
    '# All studies': ['131', '124', '64', '24', '21', '13', '4', '4', '272', '64', '50', '25', '23', '13', '2'],
    '% All studies': ['37', '35', '18', '7', '6', '4', '1', '1', '77', '18', '14', '7', '6', '4', '1'],
    '# Mixed Methods': ['14', '10', '8', '5', '2', '0', '0', '0', '27', '6', '5', '9***', '2', '1', '0'],
    '% for Mixed Methods': ['37', '26', '21', '13*', '5', '0', '0', '0', '71', '16', '13', '24', '5', '3', '0'],
    '# Nursing Journals': ['87', '74', '33', '9', '12', '10', '3', '3', '167', '37', '31', '14', '11', '10', '2'],
    '% Nursing Journals': ['41.2', '35.1', '15.6', '4.3**', '5.7', '4.7', '1.4', '1.4', '79.1', '17.5', '14.7', '6.6', '5.2', '4.7', '0.9'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
