#let's start
# motor: A,B,C,D,E
# screw: A,B,C,D,E
# pgain: 3,4,5,6
# vgain: 1,2,3,4,5
# class: 0.13 to 7.10

# import pandas as pd
# d = pd.read_csv("concrete.csv",delimiter=",",names=("no","cement","slag","flyash","water","sp","ca","fa","slump", "flow","cs"))
# d= d.iloc[1:]
# maxcs = d["cs"].max()
# print(d.loc())
# print(d.loc[d['cs']== maxcs,])

import pandas as pd
import math
d = pd.read_csv(
    "servo.csv",
    delimiter=";",
    names=("motor", "screw", "pgain", "vgain", "class"))
x = d["class"].mean()
#print(d["class"])

prox = abs((d["class"] / x) - 1)
mincls = prox.min()
print(d.loc[d['class'] == mincls, ])
