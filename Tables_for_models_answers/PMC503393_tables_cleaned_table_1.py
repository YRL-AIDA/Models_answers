headers: (0,0);(0,1);(0,2);(0,3);(0,4);(0,5);(0,6);(0,7)

import pandas as pd

df = pd.DataFrame({
    'Intervention': ['Care Coordination', 'Emergency Room', 'Hospice Care', 'Palliative Care', '', '', 'Witnessed Resuscitation'],
    'Pop': ['Relative of cancer death', 'Relative of Emergency Room Death', 'Relative of cancer death', 'Relative of cancer death', 'Relative of cancer death', 'Relative of cancer death', 'Relative of unsuccessful resuscitation'],
    'CG': ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],
    'RA': ['Y', 'N', 'Y-NE', 'Y', 'NR', 'N', 'Y'],
    'Num': ['94', '100/66', '96', '183', '119/49', '49/37', '18'],
    'Time of Evaluation': ['365 days pre-death 56 days post-death', '180–365 days post-death', '42 days post-death 540 days post-death', '60–270 days pre-death 390 days post-death', '0–60 days post-death', '365 days post-death', '30 days post-death 90 days post-death'],
    'Key Outcome Measures': ['Anxiety (HADA, Leeds Depression and Anxiety Scale); Depression (HADD, Leeds Depression and Anxiety Scale); Social Support (Family Apgar Scale)', 'Changes in satisfaction of care, information received (author-created questionnaire)', 'Depression (CES-D); Anxiety (Rand Health Insurance Study); General Health (Rand Health Insurance Study); Social Functioning', 'Grief (TRIG2)', 'Anxiety, Depression, Mental Exhaustion ("observations and ratings")', "Health, Anger, Mental State, Depression (Holland & Segroi's instrument)", 'Grief (TRIG1, TRIG2); Avoidance/Intrusion (IESA, IESI); Depression (BDI, HADD); Anxiety (HADA, BAI)'],
    'Article': ['Addington, MacDonald, et al, 1992', 'Adamowski, Dickinson, et al, 1993', 'Kane, Klein, et al, 1986', 'Ringdal, Jordhoy, et al, 2001', 'Haggmark & Theorell, 1988', 'Haggmark, Bachner, & Theorell, 1991', 'Robinson, Makenzie-Ross, et al, 1998'],
}, index=[0, 1, 2, 3, 4, 5, 6])
