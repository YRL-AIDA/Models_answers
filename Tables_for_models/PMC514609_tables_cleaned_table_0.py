import pandas as pd

df = pd.DataFrame({
    'Country (City or Region)': ['USA (Central Alabama)', 'England (Manchester)', 'Wales', 'Ireland (Belfast)', 'Ireland (Dublin)', 'Orkney Island', 'France (Brest)', 'Germany (Munich)', 'Australia (Melbourne)'],
    'Melanoma Patients (n)': ['0.3820 (123) ‡', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', '0.2350 (98) #', '0.5590 (34) ¶'],
    'Control Subjects (n)': ['0.2148 (340) ‡', '0.3257 (786) †', '0.3651 (7,165) †', '0.3422 (5,000) †', '0.3063 (1,910) †', '0.3556 (104) †', '0.3933 (150) †', '0.2170 (847) #', '0.3280 (210) ¶'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8])
