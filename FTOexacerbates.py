"""
Kristen Murphy
Horner Lab
14 June 2021
Heatmap for FTO Exacerbates IFN effect
"""
#%% Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors

#%% Import data
df = pd.read_excel("/Users/student/Box/duke_hornerlab/Lab Members/Kristen/Data from Others/siFTO IFN/Reanalyzed/Top50ISGs.xlsx")
genes = df.iloc[:,0]
mocklogFC = df.iloc[:,1]
ifnlogFC = df.iloc[:,3]
data = np.zeros((len(genes), 2))
for ind in range(len(ifnlogFC)):
   index = [mocklogFC[ind], ifnlogFC[ind]]
   data[ind] = index
var = ["Mock log FC", "IFN log FC"]

#%% Plot
plt.xticks(ticks = np.arange(len(var)), labels = var, rotation = 90, fontsize = 4)
plt.yticks(ticks = np.arange(len(genes)), labels = genes, fontsize = 4)
plt.title("Top 50 ISGs")
plt.set_cmap("inferno")
heatmap = plt.imshow(data)
plt.colorbar()
plt.savefig("FTOexacerbates.pdf", dpi = 400)