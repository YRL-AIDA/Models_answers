import pandas as pd

df = pd.DataFrame({
    'School': ["Queen's University", 'University of Toronto', 'University of Western Ontario', 'University of Ottawa', 'McMaster University'],
    'City Size': ['113,000', '4,700,000', '432,000', '823,000', '662,000'],
    '# final year medical students (2001–02)*': ['71', '167', '98', '85', '103'],
    '# residents (2001–02)*': ['248', '1268', '353', '398', '396'],
}, index=[0, 1, 2, 3, 4])
