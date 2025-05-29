import pandas as pd

df = pd.DataFrame({
    'INDIA State / Region': ['West Bengal', 'Uttar Pradesh', 'Kerala', 'Kerala', 'Gujarat', 'Himachal', 'Maharashtra', 'West Bengal', 'West Bengal', 'Sri Lanka', 'Maharashtra', 'Punjab', 'Rajasthan', 'Sri Lanka', 'Uttar Pradesh', 'Uttar Pradesh', 'total', 'northwest', 'southwest', 'northeast', 'southeast', 'central', 'total'],
    'Socio-cultural affiliation': ['Caste', 'Tribe', 'Caste', '- a', 'Caste', 'Tribe', 'Caste', 'Caste', 'Tribe', 'Caste', '- a', 'Caste', 'Caste', 'Caste', 'Tribe', 'Caste', '', '', '', '', '', '', ''],
    'Linguistic affiliation': ['Indo-European', 'Indo-European', 'Indo-European', 'Indo-European', 'Indo-European', 'Tibeto-Burman', 'Indo-European', 'Indo-European', 'Austro-Asiatic', 'Dravidic', 'Indo-European', 'Indo-European', 'Indo-European', 'Indo-European', 'Indo-European', 'Indo-European', '', '', '', '', '', '', 'Indo-European'],
    'Population': ['Mixed caste people', 'Bhoksa', 'Mixed caste people from Cochin', 'Cochin Jews', 'Mixed caste people', 'Kanet', 'Konkanastha Brahmin', 'Kurmi', 'Lodha', 'Moor', 'Parsi', 'Mixed caste people', 'Rajput', 'Sinhalese', 'Tharu', 'Uttar Pradesh Brahmin', '', '', '', '', '', '', 'Iranian'],
    'Code': ['Ben', 'Bho', 'Co', 'CoJ', 'Guj', 'Kan', 'Kon', 'Kur', 'Lod', 'Mo', 'Par', 'Pun', 'Raj', 'Sin', 'Tha', 'UPb', '', '', '', '', '', '', 'IR'],
    'n': ['50', '5', '55', '45', '53', '37', '58', '55', '56', '50', '55', '109', '35', '82', '26', '25', '796', '226', '138', '30', '6', '36', '436'],
    'N': ['80 Million', '32,000', '600,000', '5,000', '50 Million', '33,000', 'N/A', 'N/A', '59,000', '3.4 Million', '76,000', '24 Million', '5 Million', '14.6 Million', '96,000', '2.5 Million', '', '', '', '', '', '', 'ca. 68 Million'],
    '': ['', '', '', '(in Israel)', '', '', '', '', '', '', '', '', '(in Rajasthan)', '', '(in India)', '', '', '', '', '', '', '', ''],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
