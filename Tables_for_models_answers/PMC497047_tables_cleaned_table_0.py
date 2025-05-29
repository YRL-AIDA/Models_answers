headers: (0,0);(0,1);(0,2)

import pandas as pd

df = pd.DataFrame({
    'Parameter': ['Bandwidth (-3 dB)', 'DC gain', 'AC mid band gain', 'Differential mode AC input range', 'Differential mode DC input range', 'Common mode input range', 'Input noise current', 'Input bias current', 'Input impedance, Active Electrode', 'CMRR', 'Output offset', 'Input noise voltage', 'Power consumption'],
    'semi-AC-mode': ['0.32–1000 Hz', '3.22', '74 dB', '0.005–1 mV p-p', '± 370 mV', '± 2 V', '1 pA rms @ 0.1–200 Hz', '1.5 pA', '320 MΩ @ 50 Hz (1000 GΩ //10 pF)', '96 dB @ 50 Hz', '0.7 mV', '2 μV p-p (0.33 μV rms ) @ 0.1–200 Hz', '11 mW @ one channel'],
    'AC-mode': ['0.16–1000 Hz', '≈ 0', '', '', '', '', '', '', '', '', '', '', ''],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
