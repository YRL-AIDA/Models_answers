import pandas as pd

df = pd.DataFrame({
    'Subject': ['1', '2', '3'],
    'Age': ['43', '42', '21'],
    'Body weight (lb)': ['142', '138', '126'],
    'Menstrual cycle history': ['hypermenorrhea, polymenorrhea, dysmenorrhea, luteal phase deficiency', 'hypermenorrhea, polymenorrhea, dysmenorrhea', 'hypermenorrhea, dysmenorrhea'],
    'Medical conditions/health status': ['endometriosis; otherwise healthy', 'general good health', 'endometriosis; otherwise healthy'],
    'Medications': ['none', 'none', 'none'],
}, index=[0, 1, 2])
