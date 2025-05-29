import pandas as pd

df = pd.DataFrame({
    'GenBank': ['X86003', 'AB005540', 'AB005541', 'U09357', 'AI179632', 'AF034863', 'S56141'],
    'Name': ['Neuron-derived orphan receptor-2', 'PCTAIRE 2', 'PCTAIRE 3 (shown in Fig. 4)', 'Protein tyrosine phosphatase, receptor-type, Z polypeptide 1 (shown in Fig. 4)', 'Proton gated cation channel DRASIC', 'Synaptic scaffolding molecule (S-SCAM, activin receptor interacting protein 1) (shown in Fig. 4)', 'Sodium-dependent neurotransmitter transporter'],
    'Reference': ['[100]', '[101]', '[102]', '[103]', '[104]', '[105,106]', '[107]'],
}, index=[0, 1, 2, 3, 4, 5, 6])
