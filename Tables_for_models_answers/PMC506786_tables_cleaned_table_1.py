headers: (0,0);(0,1);(0,3);(1,1);(1,2);(1,3);(1,4)

import pandas as pd

df = pd.DataFrame({
    'Stage I': ['', '', 'II', '', 'III', '', '', 'VI', ''],
    'I': ['Ia', 'Ib', 'II', '', 'III', '', '', 'IV', ''],
    'Carcinoma confined to corpus': ['Length of uterine cavity ≤ 8 cm', 'Length of uterine cavity > 8 cm', 'Carcinoma involves corpus and cervix', '', 'Carcinoma extends outside uterus but not outside the true pelvis', '', '', 'Carcinoma extents outside true pelvis or involves bladder or rectum', ''],
    'Ia': ['Ib', 'Ic', 'IIa', 'IIb', 'IIIa', 'IIIb', 'IIIc', 'IVa', 'IVb'],
    'Tumor limited to endometrium': ['Invasion ≤ 1/2 myometrium', 'Invasion > 1/2 myometrium', 'Endocervical glandular involvement only', 'Cervical stromal invasion', 'Tumor invades serosa or adnexa or positive peritoneal cytology', 'Vaginal metastasis', 'Metastases to pelvic or para-aortic lymph nodes', 'Tumor invades bladder, bowel mucosa, or both', 'Distant metastases, including intra-abdominal and/or inguinal lymph nodes'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8])
