"""
Kristen Murphy
Horner Lab
22 June 2021
GO Analysis Heat Maps
"""
#%% Import Modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%% Import Data
df = pd.read_csv("/Users/student/Box/duke_hornerlab/Lab Members/Kristen/Plotting/Limma_siFTO_IFN_vs_siCTRL_IFN/GO Analysis/GOHeatmap.csv")
gocat = df.iloc[:,0]
gocat = gocat[0:10]
pval = df.iloc[:,2]
pval = pval[0:10]
data = np.zeros((len(gocat), 1))
for ind in range(len(gocat)):
    data[ind] = [pval[ind]]
var = ["Enrichment -log$_{10}$ P-Value"]

#%% Plotting
plt.xticks(ticks = np.arange(len(var)), labels = var, rotation = 90)
plt.yticks(ticks = np.arange(len(gocat)), labels = gocat, fontsize = 8)
heatmap = plt.imshow(data, cmap = "autumn")
plt.colorbar()
plt.clim([12, 16])
plt.tight_layout()
plt.savefig("GObase_bar.pdf", dpi = 300)