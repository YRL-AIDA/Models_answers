import pandas as pd

df = pd.DataFrame({
    'Medication': ['Nortriptyline', '', '', '', 'Nortriptyline and Paroxetine', 'Desipramine', 'Bupropion', 'Diazepam'],
    'Pop': ['Senior', 'Senior', 'Senior', 'Senior', 'Adult', 'Adult', 'Adult', 'Senior'],
    'CG': ['Y', 'Y', 'Y', 'N', 'N', 'N', 'N', 'Y'],
    'RA': ['Y-NE', 'Y-NE', 'NR', 'NA', 'NA', 'NA', 'NA', 'Y'],
    'Num *': ['80/66', '27/27', '30/24', '13/13', '21/15', '10/9', '22/14', '35/30'],
    'TSL (days)': ['216–279', '210 (mean)', '276', '150–750', '183–4158', 'NR', '42–56', '<14'],
    'Dose': ['Steady-state plasma level: 50–120 ng/mL', 'Steady-state plasma level: 79.9+/-28.3 ng/mL Daily dose: 70.8+/-22.2 mg', 'Steady-state plasma level: 72.7 ng/mL Daily dose: 53.0 mg', 'Daily dose: 49.2 mg', 'PT Daily dose: 20–50 mg NT Daily dose: 50–160 mg', 'Daily dose: 75–150 mg', 'Daily dose: 150–300 mg', '2 mg/pill, self-administered'],
    'DT (days)': ['112', '<180', '112', '9–184', '120', '28', '56', '<42'],
    'Key Outcome Measures': ['Depression (HAM-D); Grief (TRIG)', 'Sleep (PSQI); Depression (HAM-D, BDI)', 'Sleep (PSQI)', 'Depression (HAM-D, BDI, BSI); Grief (TRIG, JGI); Sleep (PSQI)', 'Depression (HAM-D); Grief (ICG); Sleep (PSQI)', 'Depression (HDRS, CGI, Raskin DS); Grief (Separation Distress)', 'Grief (TRIG, ICG); Depression (HAM-D)', 'Bereavement (BPQ)'],
    'Article': ['Reynolds, Miller, et al, 1999**', 'Taylor, Reynolds, et al, 1999', 'Pasternak, Reynolds, et al, 1994', 'Pasternak, Reynolds, et al, 1991', 'Zygmont, Prigerson, et al, 1998', 'Jacobs, Nelson, et al, 1987', 'Zisook, Schuchter, et al, 2001', 'Warner, Metcalfe, et al, 2001'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7])
