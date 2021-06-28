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
for ind in range(len(mocklpa)):
    if mocklpa[ind] > 2:
        bluelFC.append(mocklFC[ind])
        bluelpa.append(mocklpa[ind])

#%% Labeling Points
IFITM1m = (5.465700478, 2.362336796)
IFIT3m = (1.232024232, 12.20234018)
ISG15m = (-0.032925825, 0.022809397)
EIF2AK2m = (-0.054236867, 0.038615387)
arrow_props = dict(facecolor="black", width=0.5, headwidth=4)

#%% Broken Axes
fig = plt.figure()
bax = brokenaxes(ylims= ((-2, 30), (65, 75)))
bax.plot(mocklFC, mocklpa, "k.")
bax.plot(bluelFC, bluelpa, "b.")
bax.annotate("IFITM1", xy=IFITM1m, xytext=(4.5, 8), arrowprops=arrow_props)
bax.annotate("IFIT3", xy=IFIT3m, xytext=(0, 18), arrowprops=arrow_props)
bax.annotate("ISG15", xy=ISG15m, xytext=(0, 8), arrowprops=arrow_props)
bax.annotate("EIF2AK2", xy=EIF2AK2m, xytext=(-1.25, 8), arrowprops=arrow_props)
bax.set_xlabel('log$_{2}$ Fold Change')
bax.set_xlim([-2.5, 5.75])
bax.set_ylabel('-log$_{10}$ adj P-Value')
bax.set_title('300 ISGs (siFTO Mock/ siCTRL Mock)')
bax.grid(True)
fig.savefig("top300_ISGs_baxmock.pdf", dpi=400)
