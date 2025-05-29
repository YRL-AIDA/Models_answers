import pandas as pd

df = pd.DataFrame({
    'Vendor': ['MCW in-house', 'Electron Microscopy Sciences', 'Polysciences', 'Cel Associates', 'Asper Biotech', 'Apogent Ezrays', 'Bioslide', 'Erie Scientific', 'Genetix', 'Corning Ultra GAPS', 'Corning GAPS II', 'Sigma', 'Telechem Super Amine', 'Full Moon Biosystems'],
    'Chemistry': ['Poly-L-lysine', 'Poly-L-lysine', 'Poly-L-lysine', 'Poly-L-lysine', 'Aminated', 'Aminated', 'Aminated', 'Aminated', 'Aminated', 'Aminated', 'Aminated', 'Aminated', 'Aminated', 'Proprietary'],
    'RFU/Pixel deposited × 10 3': ['19.0+/-7.7', '15.3+/-4.9', '11.5+/-6.3', '5.7+/-3.6', '6.8+/-2.4', '6.0+/-2.9', '3.3+/-0.9', '11.5+/-4.1', '4.1+/-1.2', '2.3+/-0.3', '3.9+/-0.9', '20.7+/-3.3', '6.7+/-2.1', '6.4+/-1.4'],
    'RFU/pixel retained × 10 3': ['11.1+/-2.7', '2.12+/-1.1', '1.3+/-1.0', '2.3+/-0.5', '3.2+/-1.1', '2.8+/-0.3', '1.5+/-0.5', '3.2+/-0.9', '1.2+/-0.2', '1.5+/-0.2', '1.4+/-0.2', '5.4+/-1.0', '1.7+/-0.5', '2.1+/-0.2'],
    'Percent Retention': ['58.4%', '13.9%', '11.3%', '40.4%', '47.1%', '46.7%', '45.5%', '27.8%', '29.3%', '65.2%', '35.9%', '26.1%', '25.4%', '32.8%'],
    'Spot Diameter': ['114+/-9', '100+/-28', '125+/-6', '100+/-35', '98+/-22', '109+/-20', '93+/-7', '81+/-15', '94+/-23', '103+/-13', '117+/-18', '93+/-8', '107+/-19', '78+/-7'],
    'Processed S/(S+N)': ['0.90+/-0.00', '0.85+/-0.04', '0.86+/-0.06', '0.79+/-0.09', '0.93+/-0.05', '0.92+/-0.02', '0.87+/-0.02', '0.90+/-0.01', '0.86+/-0.02', '0.92+/-0.01', '0.92+/-0.01', '0.79+/-0.01', '0.80+/-0.0', '0.90+/-0.1'],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
