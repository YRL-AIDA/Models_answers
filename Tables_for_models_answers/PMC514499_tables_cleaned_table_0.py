headers: (0,0);(0,1)

import pandas as pd

df = pd.DataFrame({
    'Common variables during exercise test': ['Duration of exercise', 'Peak VO2', 'Anaerobic threshold', 'Oxygen pulse', 'VO2 workload ratio', 'O2 saturation'],
    'Additional echocardiographic variables during exercise test': ['Contractile reserve', 'Mitral valve function', 'Pulmonary systolic pressure', 'Right ventricular function', 'Diastolic function', ''],
}, index=[0, 1, 2, 3, 4, 5])
