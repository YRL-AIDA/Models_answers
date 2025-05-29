import pandas as pd

df = pd.DataFrame({
    'Factor': ['Office Management', '', '', 'Patient Logistics', '', '', '', '', 'Objectives', '', 'Learning Resources', '', 'Clinic Set-up', '', '', '', '', 'Preceptor Interaction', '', ''],
    'Items making up factor': ['Teaching of time management skills', 'Teaching of medical record keeping skills', 'Teaching of office management skills', 'Opportunity to see an adequate number of patients', 'Opportunity to see a large variety of patients', 'Opportunity to see patients independently', 'Readily available examination room', 'Opportunity to see patients in follow-up visits', 'Clearly defined site objectives for the rotation', 'Efforts to meet objectives made by preceptor', 'Library resources available in the clinic', 'Computer learning resources available in the clinic', 'Close proximity of clinic to campus', 'Presence of other trainees in the clinic', 'Existence of a site co-coordinator', 'Longitudinal/horizontal rotation', 'Orientation to the practice', 'Effective teachers', 'Preceptors readily available', 'Opportunity to observe preceptor if desired'],
    'Factor Loading': ['.832', '.760', '.746', '.766', '.542', '.538', '.473', '.442', '.806', '.776', '.794', '.756', '.442', '.418', '.386', '.364', '.342', '.514', '.506', '.491'],
    'Alpha Analysis': ['.62', '', '', '.69', '', '', '', '', '.53', '', '.60', '', '.55', '', '', '', '', '.55', '', ''],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
