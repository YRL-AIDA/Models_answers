headers: (0,0);(0,1);(0,2);(0,3)

import pandas as pd

df = pd.DataFrame({
    'Stage of analysis': ['', '(a)', '(b)', '(c)', 'In item bank', 'Total'],
    'Number of items removed': ['1', '28', '26', '26', '79', '160'],
    'Reason for removal': ['Concerns about the way the item was presented', "< 10% or > 90% of responses in 'cannot'", 'Significant difference between M and F and/or under and over 85 years', 'Item fit p -value < 0.01 or estimates of β i not stable', '', ''],
    'Examples': ['', 'Reaching for a cup and taking a sip of water Combing hair at a sink Cycling on a heavily laden bicycle', 'Washing up (easier for older respondents) Crossing the street (easier for younger respondents Preparing a warm meal (easier for female respondents)', 'Taking oral medication Cycling Getting money out of the bank using an ATM', 'See Table 2', ''],
}, index=[0, 1, 2, 3, 4, 5])
