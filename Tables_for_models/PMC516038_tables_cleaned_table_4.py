import pandas as pd

df = pd.DataFrame({
    'Exacerbating activity': ['Lifting heavy equipment or patients', 'Maintaining a position for a prolonged period of time', 'Transferring a patient', 'Performing repetitive tasks', 'Performing manual therapy', 'Squatting', 'Working in an awkward or cramped position', 'Climbing stairs', 'Reaching/working or cramped positions', 'Walking', 'Performing overhead activities'],
    'PT (%)': ['18.1', '16.6', '15.5', '15.8', '10.8', '5.0', '4.3', '3.9', '3.5', '3.5', '1.9'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
