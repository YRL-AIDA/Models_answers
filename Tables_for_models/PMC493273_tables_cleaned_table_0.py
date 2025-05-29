import pandas as pd

df = pd.DataFrame({
    'Trial ID': ['38', '55', '56'],
    'Study drug and dose, number of women': ['49 women Rofecoxib 25 mg Rofecoxib 50 mg Ibuprofen 400 mg Placebo', '60 women Rofecoxib 50 mg then 25 mg as required Naproxen sodium 550 mg every 12 hrs Placebo', '122 women Rofecoxib 50 mg as required Rofecoxib 50 mg then 25 mg as required Naproxen sodium 550 mg every 12 hrs Placebo'],
    'Design': ['Single oral dose, parallel 3 menstrual cycles', 'Oral. Multiple dose study with single dose efficacy data, multiple dose adverse events Cross-over, 1 of 6 drug sequences 3 menstrual cycles', 'Oral. Multiple dose study with single dose efficacy data, multiple dose adverse events Cross-over, 1 of 4 drug sequences 4 menstrual cycles'],
    'Observations after 8 hrs': ['12, 24', '12 hour obervations after a single dose in a three-day study', '12 hour obervations after a single dose in a three-day study'],
    'Quality score': ['5/5', '5/5', '5/5'],
    'Validity score': ['≥13/16', '≥13/16', '≥13/16'],
}, index=[0, 1, 2])
