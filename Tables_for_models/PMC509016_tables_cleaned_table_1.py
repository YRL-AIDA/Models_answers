import pandas as pd

df = pd.DataFrame({
    '0 h': ['7152 – spore wall assembly (sensu Saccharomyces)', '', '', '', '', '', '', '', '', '', ''],
    '9.5 h': ['', '', '', '', '', '', '', '', '', '', ''],
    '11.5 h': ['', '', '', '', '', '', '', '', '', '', ''],
    '13.5 h': ['5730 – nucleolus', '30490 – processing of 20S pre-rRNA', '7046 – ribosome biogenesis', '30515 – snoRNA binding', '', '', '', '', '', '', ''],
    '15.5 h': ['', '', '', '', '', '', '', '', '', '', ''],
    '18.5 h': ['30490 – processing of 20S pre-rRNA', '5732 – small nucleolar ribonucleoprotein complex', '5730 – nucleolus', '42273 – ribosomal large subunit biogenesis', '5842 – cytosolic large ribosomal subunit (sensu Eukarya)', '30515 – snoRNA binding', '3938 – IMP dehydrogenase activity', '6183 – GTP biosynthesis', '154 – rRNA modification', '', ''],
    '20.5 h': ['5843 – cytosolic small ribosomal subunit (sensu Eukarya)', '5842 – cytosolic large ribosomal subunit (sensu Eukarya)', '30490 – processing of 20S pre-rRNA', '5730 – nucleolus', '6414 – translational elongation', '5732 – small nucleolar ribonucleoprotein complex', '27 – ribosomal large subunit assembly and maintenance', '42273 – ribosomal large subunit biogenesis', '30515 – snoRNA binding', '3723 – RNA binding', '154 – rRNA modification'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
