import pandas as pd

df = pd.DataFrame({
    '': ['Group I (n = 37)', 'Group II (n = 9)'],
    'Preoperative Abduction': ['62.5°# (20°–85°)', '99.4°# (90°–110°)'],
    'Postoperative Abduction': ['131.4° * (90°–165°)', '140° * (110°–170°)'],
    'Abduction Gain': ['68.9° ± 22.9 # (109%)', '40.5° ± 16°# (49.5%)'],
    'Preoperative External Rotation': ['21.4° (0–80°)', '33.2° (0–65°)'],
    'Postoperative External Rotation': ['82.6° * (30°–95°)', '82.7° * (45°–90°)'],
    'External Rotation Gain': ['61.1° ± 23° (285%)', '49.5° ± 23.9° (149%)'],
}, index=[0, 1])
