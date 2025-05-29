import pandas as pd

df = pd.DataFrame({
    'Disease Category': ['Congenital lung hypoplasia Chronic lung disease of prematurity Pulmonary emphysema', 'Neonatal RDS Adult RDS', 'Pulmonary fibrosis', 'Asthma', 'Cystic fibrosis', 'Bronchiolitis obliterans', 'Lung cancer'],
    'Injured, Depleted, or Deranged Cellular Compartment*': ['Alveolar epithelium, Interstitial fibroblast, Capillary endothelium,', 'Alveolar epithelium, Capillary endothelium', 'Alveolar epithelium, Interstitial fibroblast', 'Airway epithelium, Myofibroblasts, Airway smooth muscle', 'Airway epithelium', 'Airway epithelium', 'Epithelium'],
    'Therapeutic Goals': ['Generate alveolar septa Restore complex three dimensional structure', 'Enhance surfactant production Reinforce endothelial and epithelial barriers', 'Prevent alveolar epithelial loss Inhibit fibroblast proliferation', 'Create an anti-inflammatory environment Inhibit airway wall remodeling Inhibit smooth muscle hypertrophy and hyperplasia', 'Deliver functional CFTR', 'Reinforce the epithelium against toxic, viral or immunologic injury', 'Detection, monitoring or treatment based on molecular regulation of stem cell proliferation and differentiation'],
}, index=[0, 1, 2, 3, 4, 5, 6])
