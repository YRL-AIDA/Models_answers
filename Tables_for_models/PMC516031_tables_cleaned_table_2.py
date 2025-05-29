import pandas as pd

df = pd.DataFrame({
    '': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18'],
    'Gene': ['leukemia inhibitory factor', 'epiregulin', 'interleukin 6', 'inhibitor of DNA binding 3', 'snail homolog 1', 'serum response factor', 'hexokinase 2', 'TGFB inducible early growth response', 'enigma homolog', 'Jun-B oncogene', 'vinculin', 'expressed sequence AA939927', 'B-cell translocation gene 2, anti-proliferative', 'adrenomedullin', 'methionine adenosyltransferase II, alpha', 'ELL-related RNA polymerase II', 'zyxin', 'transmembrane 4 superfamily member 10 homolog'],
    'Locus Link': ['16878', '13874', '16193', '15903', '20613', '20807', '15277', '21847', '56376', '16477', '22330', '99526', '12227', '11535', '232087', '192657', '22793', '109160'],
    'Fold change': ['32.79', '21.48', '7.84', '7.34', '6.14', '5.83', '5.43', '5.39', '5.37', '5.25', '4.54', '4.38', '3.58', '3.30', '3.28', '3.15', '2.70', '2.32'],
    'Lower CI': ['16.31', '13.61', '4.11', '5.86', '4.17', '4.39', '3.52', '3.88', '4.26', '3.12', '3.32', '3.35', '2.34', '2.79', '2.70', '2.34', '2.09', '2.11'],
    'Upper CI': ['54.48', '32.57', '12.98', '9.45', '9.00', '7.61', '7.51', '7.42', '6.93', '7.93', '6.10', '5.79', '6.09', '3.91', '3.95', '4.56', '3.37', '2.56'],
    '% decrease in DN': ['82', '54', '90', '51', '55', '53', '52', '53', '57', '61', '52', '76', '63', '47', '43', '39', '46', '39'],
    'known SRE': ['', '', '', '', '', 'YES', '', '', '', 'YES', 'YES', '', '', '', '', '', '', ''],
}, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
