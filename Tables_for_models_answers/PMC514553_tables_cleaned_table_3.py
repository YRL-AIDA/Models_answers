headers: (0,0);(0,1);(0,2);(0,3)

import pandas as pd

df = pd.DataFrame({
    'Outcome': ['% Feeling confident in helping someone ("moderately", "quite a lot" or "extremely")', 'Pre-test', 'Follow-up', 'Change (95% CI)', '% Had contact with anyone with mental health problem', 'Pre-test', 'Follow-up', 'Change (95% CI)', '% Provided help ("some" or "a lot")', 'Pre-test', 'Follow-up', 'Change (95% CI)', '% Advised professional help', 'Pre-test', 'Follow-up', 'Change (95% CI)'],
    'MHFA group': ['', '54.5%', '74.5%', '20.0% (12.6 to 27.4)', '', '71.5%', '72.9%', '1.4% (-6.9 to 9.6)', '', '37.0%', '39.0%', '2.0% (-5.5 to 9.6)', '', '28.1%', '29.4%', '1.4% (-6.8 to 9.5)'],
    'Control group': ['', '49.7%', '57.4%', '7.7% (1.3 to 14.1)', '', '70.8%', '65.6%', '-5.2% (-13.5 to 3.1)', '', '37.5%', '36.2%', '-1.3% (-9.6 to 6.9)', '', '27.1%', '16.8%', '-10.3% (-18.0 to -2.6)'],
    'P-value for group × time interaction': ['.001', '', '', '', '.157', '', '', '', '.525', '', '', '', '.007', '', '', ''],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
