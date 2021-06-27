"""
Kristen Murphy
Horner Lab
20 May 2021
Limma_siFTO_IFN_vs_siCTRL_IFN plotting
"""
#%% Import Modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from brokenaxes import brokenaxes

#%% Import Data
df = pd.read_excel("/Users/student/Box/duke_hornerlab/Lab Members/Kristen/Data from Others/siFTO IFN/Reanalyzed/Top 300 ISGs.xlsx")

#%% Sorting of Data
genenames = df.iloc[:,0]
mocklFC = df.iloc[:,8]
mocklpa = df.iloc[:,9]
ifnlFC = df.iloc[:,10]
ifnlpa = df.iloc[:,11]
ctrllFC = df.iloc[:,13]
ctrllpa = df.iloc[:,15]
bluelFC = []
bluelpa = []
for ind in range(len(ifnlpa)):
    if ifnlpa[ind] > 2:
        bluelFC.append(ifnlFC[ind])
        bluelpa.append(ifnlpa[ind])

#%% Creating the Figure
#fig, ax = plt.subplots(num = 1, clear = True)
#ax.plot(ctrllFC, ctrllpa, "k.")
#ax.plot(mocklFC, mocklpa, "k.")
#ax.plot(ifnlFC, ifnlpa, "k.")
#ax.plot(bluelFC, bluelpa, "b.")
#ax.set(xlabel = "log$_{2}$ Fold Change", ylabel = "-log$_{10}$ adj P-Value", title = "300 ISGs (siFTO IFN/ siCTRL IFN)")
#ax.grid(True)
#fig.tight_layout()
#fig.savefig("top300_ISGs_volcano_ifn_blue.pdf", dpi = 400)

#%% Broken Axes
fig = plt.figure()
bax = brokenaxes(ylims= ((-2, 50), (105, 120)))
bax.plot(ifnlFC, ifnlpa, "k.")
bax.plot(bluelFC, bluelpa, "b.")
bax.set_xlabel('log$_{2}$ Fold Change')
bax.set_ylabel('-log$_{10}$ adj P-Value')
bax.set_title('300 ISGs (siFTO IFN/ siCTRL IFN)')
bax.grid(True)
fig.savefig("top300_ISGs_baxifn.pdf", dpi=400)
