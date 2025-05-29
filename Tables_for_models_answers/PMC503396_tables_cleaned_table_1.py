headers: (0,0);(0,1);(0,2);(0,3);(0,4)

import pandas as pd

df = pd.DataFrame({
    'Factor*': ['I want to continue my education after residency', 'I enjoy pulmonary-related procedures', 'I enjoy caring for pulmonary patients', 'I like pulmonary physiology', 'I like the pulmonary faculty', 'I enjoy pulmonary inpatient coverage', 'I enjoyed working with a particular faculty member', 'I might enjoy pulmonary-related research', 'I enjoy pulmonary clinics', 'I enjoy cystic fibrosis patients', 'I enjoyed caring for a particular pulmonary patient', 'The salary would be attractive', 'I enjoy the tracheostomy/ventilator population'],
    '1992 Score': ['2.8 ± 0.4', '2.5 ± 0.8', '2.4 ± 0.5', '2.4 ± 0.8', '2.4 ± 0.5', '2.3 ± 0.5', '2.1 ± 0.9', '2.0 ± 1.2', '2.0 ± 1.0', '1.9 ± 1.1', '1.7 ± 1.3', '1.1 ± 1.2', '0.6 ± 0.5'],
    '1992 Rank': ['1', '2', '3', '3', '3', '6', '7', '8', '8', '10', '11', '12', '13'],
    '2002 Score': ['2.4 ± 0.8', '2.0 ± 1.0', '2.4 ± 0.5', '2.3 ± 0.8', '2.4 ± 0.8', '2.3 ± 0.5', '2.1 ± 0.7', '1.4 ± 0.8', '2.2 ± 0.8', '2.1 ± 1.1', '2.1 ± 0.7', '1.0 ± 0.8', '1.6 ± 1.1#'],
    '2002 Rank': ['1', '10', '1', '4', '1', '4', '7', '12', '6', '7', '7', '13', '11'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
