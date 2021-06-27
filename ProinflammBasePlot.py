"""
Kristen Murphy
Horner Lab
14 June 2021
Heatmap
"""
#%% Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%% Import data
df = pd.read_csv("/Users/student/Box/duke_hornerlab/Lab Members/Kristen/Plotting/Limma_siFTO_IFN_vs_siCTRL_IFN/Heat Map/Proinflammatory Cytokines & Chemokines.csv")
genes = df.iloc[:,4]
genes = genes[0:10]
ifnlogFC = df.iloc[:,5]
ifnlogFC = ifnlogFC[0:10]
mocklogFC = df.iloc[:,6]
mocklogFC = mocklogFC[0:10]
data = np.zeros((10,2))
for ind in range(len(ifnlogFC)):
   index = [mocklogFC[ind], ifnlogFC[ind]]
   data[ind] = index
var = ["Mock log FC", "IFN log FC"]

#%% Plot
plt.xticks(ticks = np.arange(len(var)), labels = var, rotation = 90)
plt.yticks(ticks = np.arange(len(genes)), labels = genes)
plt.title("Proinflammatory Cytokines and Chemokines                   ")
heatmap = plt.imshow(data, cmap = "inferno")
plt.colorbar(heatmap)
plt.clim(-1, 2.5)
plt.tight_layout()
plt.savefig("ProinflammatoryHeatMap.pdf", dpi = 400)