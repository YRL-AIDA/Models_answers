headers: (0,0);(0,1)

import pandas as pd

df = pd.DataFrame({
    'Intended Uses': ['Identify individual cases or clusters in a jurisdiction to prompt intervention or prevention activities', 'Identify multi-state disease outbreaks or clusters.', 'Monitor trends to assess the public health impact of the condition under surveillance.', 'Demonstrate the need for public health intervention programs and resources, as well as allocate resources.', 'Monitor effectiveness of prevention, control, and intervention activities.', 'Formulate hypotheses for further study.'],
    'Used at which level(s) of the public health system?*': ['Local, State (National)', 'State, National', 'State, National (Local)', 'State, National (Local)', 'State, National (Local)', 'National (State)'],
}, index=[0, 1, 2, 3, 4, 5])
