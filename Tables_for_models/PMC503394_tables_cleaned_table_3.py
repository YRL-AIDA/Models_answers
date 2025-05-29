import pandas as pd

df = pd.DataFrame({
    '': ['1 – 2 (1="no knowledge")', '3', '4 – 5 (5="a lot of knowledge")', 'Ever tried therapy (%)', 'Ever tried therapy for LBP (%)', 'Median helpfulness for LBP among prior users (0 to 10 scale)', 'Pain or harm reported by prior users (%)', 'Median expectation of helpfulness for current LBP (0 to 10 scale)', 'Did not provide expectation rating (%)', 'High expectations of helpfulness for current LBP (7 to 10 on 0 to 10 scale) (%)', 'Very likely to try therapy if primary care provider thought reasonable and no extra cost (%)', 'Very likely to try therapy if primary care provider thought reasonable and $10 co-pay (%)'],
    'Acupuncture (N = 249)': ['69', '17', '14', '18', '11', '5', '13', '5', '25', '19', '64', '51'],
    'Chiropractic (N = 249)': ['44', '22', '34', '54', '45', '6', '23', '5', '10', '28', '51', '42'],
    'Massage (N = 249)': ['52', '24', '24', '38', '24', '7', '13', '7', '9', '48', '69', '56'],
    'Meditation (N = 249)': ['72', '15', '13', '27', '7', '5', '5', '3', '12', '15', '27', 'NA'],
    "T'ai Chi (N = 249)": ['91', '6', '3', '8', '0.4', '**', '16', '5', '24', '16', '41', 'NA'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
