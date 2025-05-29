headers: (0,0);(0,1);(0,2);(0,3)

import pandas as pd

df = pd.DataFrame({
    'Authors': ['Tannock et al. (1996)', 'Beer et al., (2001)', 'Sinibaldi et al. (1999)', 'Copur et al. (2001)', 'Gravis et al. (2003)', 'Small et al. (2000)', 'Fuse et al. (1996)', 'Kreis et al. (1999).', 'Hamilton et al. (2003)', 'van Andel et al. (2003)', 'Kornblith et al. (2001)'],
    'Chemotherapeutic agent': ['Mitoxantrone', 'Docetaxel', 'Docetaxel', 'Docetaxel', 'Docetaxel', 'Suramin', 'Cisplatin/carboplatin', 'Docetaxel', 'Vinblastine', 'Epirubicin', 'Docetaxel'],
    'QOL measure': ['EORTC QLQ-30; Pain rating', 'Present Pain Intensity scale', 'Brief Pain Inventory', 'Numeric rating scale', 'EORTC QLQ-30; Pain VAS', 'Brief Pain Inventory', 'Rating scale', 'Physician-graded events', 'Physician-graded events', 'QLQ-30', 'FACT-P, Mental Health Inventory-17'],
    'Direction of effect': ['Improved pain, mood & physical activity', 'Improved pain', 'Improved pain', 'Improved pain', 'Improved role, social functioning, overall QOL, pain, fatigue, constipation', 'Improved pain', 'Improved pain', 'Presence of fatigue dose-limiting factor', 'Presence of fatigue dose-limiting factor', 'Reduced fatigue, transient improvement in emotional, social and cognitive functioning', 'Transient improvements in emotional well-being, improved overall QOL'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
