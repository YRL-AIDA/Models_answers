import pandas as pd

df = pd.DataFrame({
    'Type of adverse event': ['Local adverse events', 'Systemic adverse events', 'Withdrawals beacuse of adverse events', '', 'Type of adverse event', 'Local adverse events', 'Systemic adverse events', 'Withdrawals because of adverse events'],
    'Trials': ['15', '16', '10', 'Number of', 'Trials', '2', '3', '3'],
    'Patients': ['1734', '1838', '1225', '', 'Patients', '443', '764', '764'],
    'Treatment': ['53/949', '33/1002', '10/697', 'Events/total', 'Treatment', '19/243', '82/408', '19/408'],
    'Placebo': ['48/785', '14/836', '7/528', '', 'Placebo', '4/118', '87/356', '24/356'],
    'RR (95% CI)': ['1.0 (0.7 to 1.4)', '1.7 (0.96 to 2.85)', '0.9 (0.4 to 2.1)', '', 'RR (95% CI)', '3.0 (1.1 to 8.5)', '0.83 (0.6 to 1.1)', '0.7 (0.4 to 1.3)'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7])
