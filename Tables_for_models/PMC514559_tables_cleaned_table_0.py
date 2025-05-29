import pandas as pd

df = pd.DataFrame({
    'Plot': ['jh1A', 'jh1B', 'jh5', 'jh10', 'jh35', 'tk4', 'tk 22', 'matA', 'matB', 'matC'],
    'Details': ['1 year jhum fallows, cultivated and abandoned in 1998', '1 year jhum fallows, cultivated and abandoned in 1998', 'Two adjoining, indistinguishable 4–5 year jhum fields cultivated and abandoned in 1994 & 1996 respectively', 'Three adjoining, indistinguishable 7–10 year jhum fields cultivated and abandoned between 1988 & 1991', 'Five adjoining, indistinguishable 30–35 year post- jhum fields cultivated and abandoned between 1963 & 1969', '4 year old teak plantation, planted in 1994', 'Subset of a 22 year old teak plantation, planted in 1977', 'Subset of slightly disturbed contiguous mature forest', 'Subset of undisturbed contiguous mature forest', 'Subset of undisturbed contiguous mature forest'],
    'Size (ha.)': ['3–4', '3–4', '4–6', '4–6', '8–10', '3–4', '4–6', '4–6', '4–6', '4–6'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
