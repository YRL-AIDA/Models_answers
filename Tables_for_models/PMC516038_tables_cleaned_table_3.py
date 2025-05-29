import pandas as pd

df = pd.DataFrame({
    'Activity that caused injury': ['Transferring a patient', 'Performing repetitive tasks', 'Lifting heavy equipment or patients', 'Working when physically fatigued', 'Bending/twisting', 'Performing manual therapy', 'Maintaining a position for a prolonged period of the time', 'Responding to an unanticipated or sudden movement a by patient', 'Working in an awkward or cramped position', 'Slipping. tripping. falling', 'Applying modalities'],
    'PT (%)': ['14.5', '13.9', '13.6', '12.0', '11.1', '9.0', '9.2', '5.9', '5.0', '2.7', '1.5'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
