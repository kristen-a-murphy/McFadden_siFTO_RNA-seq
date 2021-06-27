"""
Kristen Murphy
Horner Lab
24 June 2021
GO Immune Breakdown
"""
#%% Import Modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%% Import Data
df = pd.read_excel("/Users/student/Box/duke_hornerlab/Lab Members/Kristen/Plotting/Limma_siFTO_IFN_vs_siCTRL_IFN/GO Analysis/ImmuneBreakdown.xlsx", sheet_name = 1)
gene = df.iloc[:,0]
logFC = df.iloc[:,3]
data = np.zeros((len(gene), 1))
for ind in range(len(gene)):
    data[ind] = [logFC[ind]]
var = ["log$_{2}$ Fold Change"]

#%% Plotting
plt.xticks(ticks = np.arange(len(var)), labels = var, rotation = 90)
plt.yticks(ticks = np.arange(len(gene)), labels = gene, fontsize = 6)
heatmap = plt.imshow(data, cmap = "autumn")
plt.colorbar(heatmap)
plt.tight_layout()
plt.savefig("GOspecific_bar.svg", dpi = 600)