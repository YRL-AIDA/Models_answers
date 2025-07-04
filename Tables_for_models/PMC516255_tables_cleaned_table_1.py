import pandas as pd

df = pd.DataFrame({
    'Window size ( L )': ['7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
    '95% Confidence Interval': ['(1.077, 1.112)', '(1.051, 1.084)', '(1.067, 1.091)', '(1.091, 1.171)', '(1.078, 1.134)', '(1.046, 1.075)', '(1.054, 1.110)', '(1.055, 1.124)', '(1.050, 1.087)', '(1.036, 1.045)', '(0.976, 1.001)', '(0.959, 0.980)', '(0.957, 0.967)', '(0.950, 0.960)'],
    '99% Confidence Interval': ['(1.072, 1.176)', '(1.046, 1.089)', '(1.061, 1.095)', '(1.078, 1.184)', '(1.068, 1.149)', '(1.042, 1.080)', '(1.047, 1.167)', '(1.044, 1.135)', '(1.044, 1.093)', '(1.030, 1.051)', '(0.977, 0.999)*', '(0.956, 0.983)', '(0.955, 0.968)', '(0.948, 0.962)'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
