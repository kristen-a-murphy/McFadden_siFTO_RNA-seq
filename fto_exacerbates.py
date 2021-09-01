"""
Kristen Murphy
Horner Lab
12 August 2021
FTO exacerbates heatmap 3 cols
Reviewer Comment adjustments
"""
#%% Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors

#%% Import data
df = pd.read_excel("/Users/kristenmurphy/Box/duke_hornerlab/Lab Members/Kristen/Data from Others/siFTO IFN/Reanalyzed/Top50ISGs.xlsx")

#%% Sorting data
genes = df.iloc[:,0]
genes1 = genes[0:24]
genes2 = genes[25:49]
# siCTRL IFN vs siCTRL Mock
col1 = df.iloc[:,6]
col1_1 = col1[0:24]
col1_2 = col1[25:49]

#%% Setting up for Plotting
data1 = np.zeros((len(genes1), 2))
data2 = np.zeros((len(genes2), 2))
# first part fof data is mock so will be set to one since IFN is log fold change over mock
for ind in range(len(col1_1)):
    index = [1, col1_1[ind]] 
    data1[ind] = index
for ind in range(len(col1_2)):
    newind = ind+25
    index = [1, col1_2[newind]]
    data2[ind] = index
var = ["siCTRL Mock", "siCTRL IFN"]

#%% Plotting
plt.xticks(ticks = np.arange(len(var)), labels = var, rotation = 90, fontsize = 7)
# for left side
plt.yticks(ticks = np.arange(len(genes1)), labels = genes1, fontsize = 7)
# for right side
#plt.yticks(ticks = np.arange(len(genes2)), labels = genes2, fontsize = 7)

plt.set_cmap("inferno")
heatmap = plt.imshow(data1)
#heatmap = plt.imshow(data2)
plt.colorbar(heatmap)
#plt.clim([-1.5, 4.5])
plt.clim([-0.5, 12])
plt.savefig("control_mock_v_ifn_1.pdf", dpi = 400)
#plt.savefig("fto_exacerbates_2.png", dpi=400)