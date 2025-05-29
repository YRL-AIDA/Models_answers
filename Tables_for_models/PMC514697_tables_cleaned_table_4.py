import pandas as pd

df = pd.DataFrame({
    'Program variant': ['pknotsRG-mfe', 'pknotsRG-loc', 'pknotsRG-enf'],
    'Nonterminals': ['27', '27', '40'],
    'Productions': ['74', '68', '119'],
    'Tables': ['8', '8', '11'],
}, index=[0, 1, 2])
