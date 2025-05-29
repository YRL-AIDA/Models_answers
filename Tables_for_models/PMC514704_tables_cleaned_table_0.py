import pandas as pd

df = pd.DataFrame({
    'Diagnosis': ['BA', 'BA', 'BA', 'BA', 'BA', 'BA', 'BA', 'BA', 'BA', 'BA', 'BA', 'BA', 'BA', 'BA', 'BA', 'NH', 'NH', 'NH', 'NH'],
    'Chimerism': ['Present', 'Present', 'Present', 'Present', 'Present', 'Not interpretable', 'Present', 'Present', 'Not interpretable', 'Not interpretable', 'None detected', 'Present', 'Present', 'Present', 'Present', 'None detected', 'None detected', 'Not interpretable', 'Not interpretable'],
    'Method': ['FISH', 'FISH', 'FISH', 'FISH', 'FISH+immunokistochemistry', 'FISH', 'FISH', 'FISH', 'FISH', 'FISH', 'FISH', 'kPCR', 'kPCR', 'kPCR', 'kPCR', 'FISH', 'FISH', 'FISH', 'FISH'],
    "# of Maternal cells/DNA per slide (FISH) or per 25,000 copies of patient's DNA (kPCR)": ['2 maternal cells per slide', '2 maternal cells per slide', '4 maternal cells per slide', '2 maternal cells per slide', '3 maternal cells per slide', '---', '2 maternal cells per slide', '3 maternal cells per slide', '---', '---', '0 maternal cells per slide', "3 copies of maternal DNA per 25,000 copies of patient's DNA", "1 copy of maternal DNA per 25,000 copies of patient's DNA", "10 copies of maternal DNA per 25,000 copies of patient's DNA", "142 copies of maternal DNA per 25,000 copies of patient's DNA", '0 maternal cells per slide', '0 maternal cells per slide', '---', '---'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
