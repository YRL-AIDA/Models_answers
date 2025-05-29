import pandas as pd

df = pd.DataFrame({
    'GenBank': ['X74832', 'M16112', 'M88469', 'AF060879', 'U16845', 'M96375', 'X89963', 'AF030089', 'D88250'],
    'Name': ['Acetylcholine receptor alpha subunit (cholinergic receptor, nicotinic, alpha polypeptide 1)', 'Brain type II calcium/calmodulin dependent protein kinase beta subunit', 'F-spondin (shown in Fig. 5)', 'Neurocan (chondroitin sulfate proteoglycan 3)', 'Neurotrimin', 'Non-processed neurexin 1-beta (neurexin 1)', 'TSP-4 (thrombospondin-4) (shown in Fig. 5)', 'Activity and neurotransmitter-induced early gene 4 (ania-4) (shown in Fig. 5)', 'Serine protease (complement component 1, s subcomponent)'],
    'Reference': ['[108]', '[109]', '[110]', '[111,112]', '[113]', '[114]', '[115–117]', '[118]', '[119]'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8])
