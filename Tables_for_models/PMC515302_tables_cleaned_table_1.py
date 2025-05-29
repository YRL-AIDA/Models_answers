import pandas as pd

df = pd.DataFrame({
    'Year': ['2003', '1998', '1993', '1988', '1983'],
    'Vol': ['326-7', '316-7', '306-7', '296-7', '286-7'],
    'Trials': ['9', '4', '4', '0', '1'],
    'Clustering ignored': ['0', '1(?)', '3', '0', '1'],
    'Ignoring clustering judged as important': ['0', '1', '2', '0', '1'],
    'Found in Web of Science search': ['5', '0', '0', '0', '0'],
}, index=[0, 1, 2, 3, 4])
