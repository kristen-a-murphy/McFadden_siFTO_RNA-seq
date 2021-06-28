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

#%% Labeling Points
IFITM1i = (1.872308339, 0.666572553)
IFIT3i = (0.723889308, 9.335840263)
ISG15i = (0.558765087, 1.372606944)
EIF2AK2i = (-0.494120453, 1.031231649)
arrow_props = dict(facecolor="black", width=0.5, headwidth=4)

#%% Broken Axes
fig = plt.figure()
bax = brokenaxes(ylims= ((-2, 70), (100, 110)))
bax.plot(mocklFC, mocklpa, "k.")
bax.plot(bluelFC, bluelpa, "b.")
bax.annotate("IFITM1", xy=IFITM1i, xytext=(2.25, 6), arrowprops=arrow_props)
bax.annotate("IFIT3", xy=IFIT3i, xytext=(0, 21), arrowprops=arrow_props)
bax.annotate("ISG15", xy=ISG15i, xytext=(-0.5, 13), arrowprops=arrow_props)
bax.annotate("EIF2AK2", xy=EIF2AK2i, xytext=(-2, 12), arrowprops=arrow_props)
bax.set_xlabel('log$_{2}$ Fold Change')
bax.set_xlim([-2.5, 5.75])
bax.set_ylabel('-log$_{10}$ adj P-Value')
bax.set_title('300 ISGs (siFTO IFN/ siCTRL IFN)')
bax.grid(True)
fig.savefig("top300_ISGs_baxifn.pdf", dpi=400)
