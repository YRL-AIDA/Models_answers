import pandas as pd

df = pd.DataFrame({
    'Genbank': ['M31725', 'S82649', 'X59149', 'L08496', 'S68944', 'S76742', 'U39549', 'D28512', 'AF007758', 'AF081557', 'L15305', 'M24852', 'D17521'],
    'Name': ['Axonal glycoprotein TAG-1 (Contactin 2) (shown in Fig. 2)', 'Neuronal activity-regulated pentraxin (Narp)', 'Neural cell adhesion molecule L1', 'GABA-A receptor delta subunit', 'Na + /Cl - -dependent neurotransmitter transporter', 'Neurotransmitter transporter rB21a (X transporter protein 3)', 'Synaptogyrin (synaptogyrin 1)', 'Synaptotagmin III (synaptotagmin 3)', 'Synuclein 1 (synuclein alpha)', 'Glial cells missing protein homolog (Gcm1, glial cells missing homolog a)', 'Glial-derived neurotrophic factor', 'Neuron-specific protein PEP-19 (Purkinje cell protein 4)', 'Protein kinase C-regulated chloride channel'],
    'Reference': ['[74]', '[75]', '[76–78]', '[79]', '[80]', '[81]', '[82]', '[83]', '[84]', '[85]', '[86]', '[87]', '[88]'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
