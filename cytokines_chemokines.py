"""
Kristen Murphy
Horner Lab
12 August 2021
Proinflammatory Chemokines and Cytokines Heatmap
"""
#%% Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%% Import data
df = pd.read_csv("/Users/kristenmurphy/Box/duke_hornerlab/Lab Members/Kristen/Plotting/Limma_siFTO_IFN_vs_siCTRL_IFN/Heat Map/Proinflammatory/Proinflammatory Cytokines & Chemokines.csv")

#%% Sort and Set up Data
genes = df.iloc[:,0]
genes = genes[0:10]
siCTRL = df.iloc[:,1]
siCTRL = siCTRL[0:10]
#siFTO = df.iloc[:,2]
#siFTO = siFTO[0:10]
#IFN_FTO_vs_CTRL = df.iloc[:,3]
#IFN_FTO_vs_CTRL = IFN_FTO_vs_CTRL[0:10]
data = np.zeros((10,2))
for ind in range(len(siCTRL)):
   index = [1, siCTRL[ind]]
   data[ind] = index
var = ["siCTRL Mock", "siCTRL IFN"]

#%% Plot
plt.xticks(ticks = np.arange(len(var)), labels = var, rotation = 90)
plt.yticks(ticks = np.arange(len(genes)), labels = genes)
heatmap = plt.imshow(data, cmap = "inferno")
plt.colorbar(heatmap)
#plt.tight_layout()
plt.savefig("proinflammatory_heatmap.pdf", dpi = 400)