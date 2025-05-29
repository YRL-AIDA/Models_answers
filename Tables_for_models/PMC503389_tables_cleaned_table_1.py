import pandas as pd

df = pd.DataFrame({
    'Gene': ['MT1-MMP', 'MMP-11', '18s rRNA'],
    "5' sequence": ['gACAgTACACCCTTTgATggTgAA', 'CCTTCCAggATgCTgAgggCTAT', 'TCAAGAACgAAAgTCggAgg'],
    "3' sequence": ['gATCgTTAgAATgTTCCAggCCTA', 'ATgACAgCATggTCgTTCCTACAA', 'ggACATCTAAgggCATCACA'],
    'Standard amplicon': ['197 bp', '330 bp', '490 bp'],
    "Competitor sequence (standard 5' primer plus)": ['CAgGCCCCAATATTggAggggAT', 'TCTCTACTggAggTTTgATCCCgT', 'N/A'],
    'Competitor amplicon': ['169 (-28 bp)', '310 (-20 bp)', 'N/A'],
}, index=[0, 1, 2])
